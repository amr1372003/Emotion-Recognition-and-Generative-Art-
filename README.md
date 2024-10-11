# Emotion Recognition with Generative Art 🎨

This project combines emotion recognition using machine learning and real-time generative art. The system detects human emotions via a webcam and reflects the emotions as dynamic color changes in a visual flow field on a web page.

## Project Overview
. Emotion Detection: Utilizes OpenCV for face detection and DeepFace for emotion recognition.
. Web App: The frontend visualizes the detected emotions with JavaScript and Perlin Noise, creating a flow field with colors changing according to emotions.
. Server: A Flask server communicates between the Python-based emotion detection and the web app, sending emotion data in real-time.
Directory Structure
## AI Folder:
Contains the working server (main_server.py) responsible for running the complete emotion recognition system and communicating with the web app.

## Web Folder:
Contains a demo server (demo_server.py), which can be used to simulate emotions for demonstration purposes. This server is for demonstration only and does not perform real-time face recognition.

main.py:
The Python script that runs face recognition only. It does not handle server communication. For full functionality, use main_server.py.

Key Files
main_server.py:
Runs the Flask server and handles both face recognition and emotion analysis. It sends the recognized emotion to the web interface for real-time visualization.

main.py:
Performs face recognition using OpenCV and DeepFace. This file is standalone and does not include server communication.

demo_server.py (in Web folder):
A simplified Flask server that can be used to simulate emotion data for demonstration purposes. It does not analyze emotions.

index.html (in Web folder):
The frontend webpage that visualizes emotions through a flow field created using Perlin noise. The colors change based on emotions.

## Setup Instructions
Prerequisites
Python 3.x
OpenCV
DeepFace
Flask
JavaScript (Frontend)

## How to Run
Clone the repository.

## Install dependencies:
```bash
pip install opencv-python Flask deepface
```

## Start the server:
### For full functionality with face and emotion recognition, run main_server.py:
```bash
python AI/main_server.py
```

### For demonstration without real-time recognition, run demo_server.py:
```bash
python Web/demo_server.py
```

## Access the web interface:
Open index.html in your browser (located in the Web folder).

If running the working server (main_server.py), ensure that it is running on the same machine as the web page.

## Usage
The system detects emotions like happiness, sadness, and anger.
The web page visualizes these emotions using a flow field where:
Happy is shown in warm reds and oranges.
Sad is visualized in calming blues.
Angry is depicted in intense reds.
Neutral appears in grayscale tones.

## Notes
The working server is located in the AI folder (main_server.py).
The demo server in the Web folder (demo_server.py) is only for demonstration purposes and does not perform face or emotion recognition.
