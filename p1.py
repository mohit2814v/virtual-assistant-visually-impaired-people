import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        command = ""
        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
        return command

def run_virtual_assistant():
    speak("Hello! I am your virtual assistant. How can I help you today?")
    
    while True:
        command = listen()
        
        if 'play music' in command:
            song = command.replace('play music', '')
            speak(f'Playing {song} on YouTube.')
            pywhatkit.playonyt(song)

        elif 'time' in command:
            current_time = datetime.datetime.now().strftime("%H:%M")
            speak(f"The current time is {current_time}.")

        elif 'who is' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, sentences=1)
            speak(info)

        elif 'tell me a joke' in command:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'news' in command:
            response = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=YOUR_API_KEY")
            news_data = response.json()
            articles = news_data['articles']
            for article in articles[:5]:  # Read top 5 news articles
                speak(article['title'])

        elif 'stop' in command:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    run_virtual_assistant()

# Example usage
while True:
    command = listen()
    if "news" in command.lower():
        speak("Fetching the latest news.")
        # Fetch news logic here
    elif "navigate" in command.lower():
        speak("Starting navigation.")
        # Navigation logic here
import cv2

def detect_objects(frame):
    # Load pre-trained model and perform detection
    # Return detected objects with descriptions
    pass  # Implement object detection logic here
import cv2
import numpy as np
import speech_recognition as sr
from transformers import pipeline

# Initialize the video capture
video_path = 'input_video.mp4'
cap = cv2.VideoCapture(video_path)

# Initialize speech recognition
recognizer = sr.Recognizer()

# Function to extract keyframes
def extract_keyframes(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []
    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if frame_count % 30 == 0:  # Extract one frame every second (assuming 30fps)
            frames.append(frame)
        frame_count += 1
    cap.release()
    return frames

# Function to transcribe audio from video
def transcribe_audio(video_path):
    with sr.AudioFile(video_path) as source:
        audio = recognizer.record(source)
        return recognizer.recognize_google(audio)

# Function to summarize text using transformers
def summarize_text(text):
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']

# Main execution flow
keyframes = extract_keyframes(video_path)
transcript = transcribe_audio('audio.wav')  # Assuming audio has been extracted separately
summary = summarize_text(transcript)

# Display results
print("Video Summary:", summary)
for i, frame in enumerate(keyframes):
    cv2.imshow(f'Keyframe {i+1}', frame)
    cv2.waitKey(1000)  # Display each frame for a second

cv2.destroyAllWindows()
