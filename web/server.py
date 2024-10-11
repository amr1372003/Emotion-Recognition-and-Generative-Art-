from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

mood = "default"

@app.route('/update_mood', methods=['POST'])
def update_mood():
    global mood
    mood = request.json.get('mood', 'default')
    return jsonify({"status": "success", "mood": mood}), 200

@app.route('/get_mood', methods=['GET'])
def get_mood():
    return jsonify({"mood": mood}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0')

    #to run server: python server.py
    # to change mood: curl -X POST http://localhost:5000/update_mood -H "Content-Type: application/json" -d '{"mood": "happy"}'
