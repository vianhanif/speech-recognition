import platform
import pyttsx

# see http://pyttsx.readthedocs.org/en/latest/engine.html#pyttsx.init
class Robot:
    speech_engine = None

    def __init__(self, rate=200):
        self.speech_engine = pyttsx.init(self.getEngine())
        self.speech_engine.setProperty("rate", rate)

    def getEngine(self):
        return {
            "Windows" : "sapi5",
            "Linux" : "espeak",
            "Darwin" : "nsss"
            }[platform.system()]

    def setRate(self, rate):
        self.speech_engine.setProperty("rate", rate)

    def getRate(self):
        return self.rate

    def speak(self, sentences):
        self.speech_engine.say(sentences)
        self.speech_engine.runAndWait()
