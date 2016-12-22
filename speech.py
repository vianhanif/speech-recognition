# -*- coding: utf-8 -*-
import platform
import pyttsx
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# see http://pyttsx.readthedocs.org/en/latest/engine.html#pyttsx.init
class Robot:
    speech_engine = None
    robot = None
    name = ""

    def __init__(self, rate=130, name="Ryuji", intro="Hi There."):
        self.speech_engine = pyttsx.init(self.getEngine())
        self.speech_engine.setProperty("rate", rate)
	self.robot = ChatBot(
            name,
            logic_adapters=[
                {
                    'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                    'threshold': 0.65,
                    'default_response': 'I am sorry, but I do not understand.'
                }
            ]
        )
	self.robot.set_trainer(ListTrainer)
	self.name = name
	self.speak("%s. My name is %s. You can ask me anything " % (intro, name))

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

    def get_name(self):
	return self.name

    def train(self, conversation=[]):
	self.robot.train(conversation)

    def response(self, responsee=""):
        words = self.robot.get_response(responsee)
	self.speak(words)
	print "answer : %s" % (words)

    def export_corpus(self):
        self.robot.trainer.export_for_training("./corpus.json")
    
	
		
