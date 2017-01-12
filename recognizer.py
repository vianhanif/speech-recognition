# -*- coding: utf-8 -*-
import speech_recognition as sr
import time
import urllib2 as internet
import socket
from socket import AF_INET, SOCK_DGRAM
from os import path

class Recognition:
    speech = None
    recognizer = ""
    audio = None
    data = None
    audio_file = None
    error = False
    URL = "http://216.58.192.142"

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
            with sr.Microphone(sample_rate=44100) as source:
                print("Listening to microphone...")
                self.speech.adjust_for_ambient_noise(source)
                self.audio = self.speech.listen(source)

    def isConnected(self):
        try:
            internet.urlopen(self.URL, timeout=1)
            return True
        except internet.URLError as err:
            return False
        except socket.timeout:
            #print("time out")
            return False
    
    def getRecognizer(self):
        #_internet = self.isConnected()
        _recognizer = ("sphinx")
        #print("Testing connection to " + self.URL + " : " + ("success" if _internet else "failure"))
        #print("Trying to recognize with " + _recognizer + "...")
        print("responding...")
        return {
            "google" : self.speech.recognize_google,
            "sphinx" : self.speech.recognize_sphinx
            }[_recognizer](self.audio)

    def recognize(self):
        try:
            self.data = self.getRecognizer()
            print("Recorded : '" + self.data + "'")
            return True
        except sr.UnknownValueError:
            self.error = True
            print("Bot could not understand audio")
            return False
        except sr.RequestError as e:
            self.error = True
            print("Bot error; {0}".format(e))
            return False

    def getAudio(self):
        return self.audio
    
    def getText(self):
        return self.data if not self.error else ""
