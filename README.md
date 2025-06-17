Transcribing Audio to Text


A straightforward and effective Python script that converts spoken words from an audio file into written text. This project leverages the power of the SpeechRecognition library to provide accurate transcriptions.

## 📝 Table of Contents

About the Project
Getting Started
Prerequisites
Installation
Usage
How It Works
Contributing
License
Author
📖 About The Project
This project provides a simple solution for transcribing audio files. It's designed to be a lightweight and easy-to-use tool for anyone needing to convert audio recordings into text, whether for documentation, analysis, or accessibility purposes. The script reads an audio file and uses Google's powerful speech recognition engine to generate a text transcription.

🚀 Getting Started
Follow these instructions to get a copy of the project up and running on your local machine.

Prerequisites
Ensure you have Python 3 and pip (Python package installer) installed on your system.

Python 3
Bash

python --version
Pip
Bash

pip --version
Installation
Clone the repository:
Bash

git clone https://github.com/sainikhilchidipothu/Transcribing-Audio-to-Text.git
Navigate to the project directory:
Bash

cd Transcribing-Audio-to-Text
Install the required Python package: The project relies on the SpeechRecognition library.
Bash

pip install SpeechRecognition
Usage
Running the script is simple.

Place the audio file you want to transcribe into the project directory.
Open the Transcribing audio to text.py file and update the filename on this line to match your audio file:
Python

# Change 'OSR_us_000_0010_8k.wav' to your audio file's name
with sr.AudioFile('OSR_us_000_0010_8k.wav') as source:
Execute the script from your terminal:
Bash

python "Transcribing audio to text.py"
 ```
4.  The script will process the audio and print the transcribed text to the console.

Example Output:

the stale smell of old beer lingers it takes heat to bring out the odor a cold dip restores health and zest a salt pickle tastes fine with ham tacos al pastor are my favorite a zestful food is the hot cross bun
##⚙️ How It Works

The script uses the speech_recognition library, a popular Python library for performing speech recognition with various engines and APIs.

Initialization: An instance of the Recognizer class is created.
Audio Input: The script opens the specified audio file (.wav format) using sr.AudioFile.
Audio Processing: The recognizer.record() method reads the audio data from the file.
Recognition: The recognizer.recognize_google() method sends the audio data to the Google Web Speech API.
Output: The API returns the transcribed text, which the script then prints to the console.
🤝 Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

Fork the Project
Create your Feature Branch (git checkout -b feature/AmazingFeature)
Commit your Changes (git commit -m 'Add some AmazingFeature')
Push to the Branch (git push origin feature/AmazingFeature)
Open a Pull Request
Don't forget to give the project a star! Thanks again!

📜 License
Distributed under the MIT License. See LICENSE for more information.

👨‍💻 Author
Sai Nikhil Chidipothu

GitHub: @sainikhilchidipothu
