# -*- coding: utf-8 -*-
import platform
import pyttsx
import time
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.response_selection import get_random_response

# see http://pyttsx.readthedocs.org/en/latest/engine.html#pyttsx.init
class Robot:
    speech_engine = None
    robot = None
    name = ""
    voices = None

    def __init__(self, rate=130, name="Ryuji", intro="Hi There.", language='\x05zh-yue'):
        self.speech_engine = pyttsx.init(self.getEngine())
        self.speech_engine.setProperty("rate", rate)
	self.voices = self.speech_engine.getProperty('voices')
	for voice in self.voices:
		if str(voice.languages[0]) == language:
			self.speech_engine.setProperty('voice', voice.id)
	self.robot = ChatBot(
            name,
            response_selection_method=get_random_response,
            logic_adapters=[
                'app.ChatAdapter',
                'chatterbot.logic.BestMatch'
            ]
        )
	self.robot.set_trainer(ListTrainer)
	self.name = name
	try:
            self.speech_engine.startLoop(False)
        except (RuntimeError):
            print("")
            

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
        #self.speech_engine.runAndWait()
	self.speech_engine.iterate()

    def get_name(self):
	return self.name

    def train(self, conversation=[]):
	self.robot.train(conversation)

    def response_text(self, responsee):
	return self.robot.get_response(responsee)

    def response(self, responsee=""):
        words = self.robot.get_response(responsee)
	self.speak(words)
	print "answer : %s" % (words)

    def export_corpus(self):
        self.robot.trainer.export_for_training("./src/corpus.json")

    def __exit__(self, type, value, traceback):
        self.speech_engine.endLoop()
    
	
		
