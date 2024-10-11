import cv2
from deepface import DeepFace as DF

# Load the face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Open webcam
video = cv2.VideoCapture(0)

if not video.isOpened():
    raise IOError('Cannot open webcam')

while video.isOpened():
    ret, frame = video.read()

    if not ret:
        print("Failed to capture frame")
        break

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

            dominant_emotion = result['dominant_emotion']

            # Draw emotion label on the frame
            cv2.putText(frame, dominant_emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (224, 77, 176), 2)

            # Print the dominant emotion
            print(dominant_emotion)

        except Exception as e:
            print(f"No face or emotion analysis failed: {e}")

    # Show the frame with the detected face and emotion
    cv2.imshow('Video', frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close windows
video.release()
cv2.destroyAllWindows()
