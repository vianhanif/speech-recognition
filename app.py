# -*- coding: utf-8 -*-
from recognizer import Recognition
from speech import Robot
import time

speech = Recognition()
robot = Robot()
conversation = [
	"My Name is",
	"Nice to meet you",
	"Nice to meet you too",
	"I'll be happy to answer your question",
	"What is your favorite",
	"I don't have any interest of anykind",
	"I am a",
	"Well. Hi there",
	"I am fine ",
	"Happy to hear that",
	"Bye",
	"See you next time",
        "Hello",
        "Hi there!",
        "How are you?",
        "I'm doing great.",
        "What's your name?",
        ("My name is %s" % (robot.get_name())),
        "Thank You",
        "Bye",
        "What are you?",
        "I am a Bot designed to introduce Speech Recognition program",
	"What do you do?",
	"I introduce people about Speech Recognition program"
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
