# -*- coding: utf-8 -*-
"""
Flask application for transcribing audio files.
To run:
1. Make sure you have Flask and SpeechRecognition installed:
   pip install Flask SpeechRecognition
2. Create a folder named 'templates' in the same directory as this script.
3. Place the 'index.html' file inside the 'templates' folder.
4. Run this script from your terminal: python app.py
5. Open your web browser and go to http://127.0.0.1:5000
"""
import speech_recognition as sr
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os

# Initialize the Flask application
app = Flask(__name__)
# Create an upload folder if it doesn't exist
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    """Renders the main page."""
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
    """Handles the audio file upload and transcription."""
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if file:
        # Save the file securely
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Initialize the recognizer
        r = sr.Recognizer()

        # Process the audio file
        with sr.AudioFile(filepath) as source:
            audio_data = r.record(source)
            try:
                # Recognize speech using Google Web Speech API
                text = r.recognize_google(audio_data)
                # Return the transcribed text as JSON
                return jsonify({'text': text})
            except sr.UnknownValueError:
                # Handle cases where speech is unintelligible
                return jsonify({'error': 'Audio was unintelligible.'}), 400
            except sr.RequestError as e:
                # Handle API request errors
                return jsonify({'error': f'Could not request results from Google Speech Recognition service; {e}'}), 500
            finally:
                # Clean up by removing the uploaded file
                os.remove(filepath)
    
    return jsonify({'error': 'An unknown error occurred'}), 500

if __name__ == '__main__':
    # Run the app in debug mode
    app.run(debug=True)
