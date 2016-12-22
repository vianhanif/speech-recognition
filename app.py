# -*- coding: utf-8 -*-
from recognizer import Recognition
from speech import Robot
import time

speech = Recognition()
robot = Robot()
conversation = [
        "Hello",
        "Hi there!",
        "How are you?",
        "I'm doing great.",
        "What's your name?",
        ("My name is %s" % (robot.get_name())),
        "bye",
        "See you",
        "What is your favorite food?",
        "I like anykind of food",
        "What are you?",
        "I am a Bot designed to introduce Speech Recognition program",
]

def main():
	say = ""
	robot.train(conversation)
	while say != "thank you":
                try:
                        if say != "":
                                robot.response(say)
                        speech.listen()
                        if speech.recognize():
                                say = speech.getText()
                except (KeyboardInterrupt, EOFError, SystemExit):
                        robot.export_corpus()

if __name__ == '__main__':main()
