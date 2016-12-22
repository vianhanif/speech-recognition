
from recognizer import Recognition
from speech import Robot

speech = Recognition()
robot = Robot()

def main():
	say = ""
        try:
                while say != "thank you":
			if say != "":
				robot.response(say)
			else:
				print "listening..."
				speech.listen()
				if speech.recognize():
					say = speech.getText()
	except (KeyboardInterrupt, EOFError, SystemExit):
		robot.speak("Thank you for your time")

if __name__ == '__main__':main()
