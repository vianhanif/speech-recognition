# -*- coding: utf-8 -*-
from recognizer import Recognition
from robot import Robot
from corpus import CorpusTrainer
from corpus_data import CorpusData
import time
import sys

speech = Recognition()
robot = Robot()
CorpusTrainer(robot, CorpusData(robot).getCorpus())

say = ""
def ask(say):
	try:
		if str(robot.response_text(say)).lower() == "bye":
			robot.response(say)
			robot.export_corpus()
			time.sleep(3)
			sys.exit()
	        if say != "":
                	robot.response(say)
                        #speech.listen()
			say = raw_input("user :")
			ask(say)
                        #if speech.recognize():
                                #say = speech.getText()
	except (KeyboardInterrupt, EOFError, SystemExit):
        	robot.export_corpus()

def main():
        robot.speak("Hi There. My name is %s. What is your name?" % (robot.get_name()))
	say = raw_input("user :")
	ask(say)
                

if __name__ == '__main__':main()
