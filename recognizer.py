import speech_recognition as sr
import time
from os import path

class Recognition:
    speech = None
    recognizer = ""
    audio = None
    data = None
    error = ""
    audio_file = None

    def __init__(self, recognizer = "sphinx"):
        self.speech = sr.Recognizer()
        self.recognizer = recognizer

    def listen(self, resources=""):
        if resources:
            self.audio_file = path.join(path.dirname(path.realpath(__file__)), resources)
            with sr.AudioFile(self.audio_file) as source:
                print("Recording...")
                self.audio = self.speech.record(source)
        else:
            with sr.Microphone() as source:
                print("Listening to microphone...")
                self.speech.adjust_for_ambient_noise(source)
                self.audio = self.speech.listen(source)
        
    def getRecognizer(self):
        print("Trying to recognize with " + self.recognizer + "...")
        return {
            "sphinx" : self.speech.recognize_sphinx(self.audio),
            "google" : self.speech.recognize_google(self.audio),
            }[self.recognizer]

    def recognize(self):
        try:
            self.data = self.getRecognizer()
        except sr.UnknownValueError:
            self.error = "Bot could not understand audio"
        except sr.RequestError as e:
            self.error = "Bot error; {0}".format(e)

    def getAudio(self):
        return self.audio
    
    def getText(self, split = "none"):
        return {
            "none" : self.data,
            "split": self.data.split()
            }[split] if not self.error else self.error
