import cv2
from deepface import DeepFace as DF
from flask import Flask, request, jsonify
from flask_cors import CORS
import threading

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize global mood
mood = "default"

# Flask route to update the mood
@app.route('/update_mood', methods=['POST'])
def update_mood():
    global mood
    mood = request.json.get('mood', 'default')
    return jsonify({"status": "success", "mood": mood}), 200

# Flask route to get the current mood
@app.route('/get_mood', methods=['GET'])
def get_mood():
    return jsonify({"mood": mood}), 200

# Function to run emotion detection with OpenCV and DeepFace
def detect_emotion():
    global mood

    # Load the face detection model
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Open webcam
    video = cv2.VideoCapture(0)

    if not video.isOpened():
        raise IOError('Cannot open webcam')

    # Define scale factor (reduce to 50% of the original size)
    scale_factor = 0.5

    while video.isOpened():
        ret, frame = video.read()

        if not ret:
            print("Failed to capture frame")
            break

        # Resize the frame to scale it down
        frame = cv2.resize(frame, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_LINEAR)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

        # Debug: Print number of faces detected
        print(f"Faces detected: {len(faces)}")

        for (x, y, w, h) in faces:
            # Extract the face region from the frame
            face_roi = frame[y:y+h, x:x+w]

            # Draw rectangle around face
            cv2.rectangle(frame, (x, y), (x + w, y + h), (89, 2, 236), 2)

            try:
                # Analyze emotions in the face region
                result = DF.analyze(face_roi, actions=['emotion'])

                # Check if result is a list or a dictionary
                if isinstance(result, list):
                    result = result[0]  # Access the first result if a list is returned

                # Get the dominant emotion
                dominant_emotion = result['dominant_emotion']

                # Print the dominant emotion
                print(f"Detected Emotion: {dominant_emotion}")

                # Update the global mood in Flask server
                mood = dominant_emotion

                # Draw the emotion text above the face rectangle
                text_position = (x, y - 20)  # Adjusted position so it's higher above the rectangle
                cv2.putText(frame, dominant_emotion, text_position, cv2.FONT_HERSHEY_SIMPLEX, 1, (224, 77, 176), 2)

            except Exception as e:
                print(f"No face or emotion analysis failed: {e}")

        # Show the scaled-down frame with the detected face and emotion
        cv2.imshow('Video', frame)

        # Exit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture and close windows
    video.release()
    cv2.destroyAllWindows()

# Run Flask app and emotion detection in parallel
if __name__ == '__main__':
    # Run the emotion detection in a separate thread
    threading.Thread(target=detect_emotion).start()

    # Start the Flask server
    app.run(host='0.0.0.0')
