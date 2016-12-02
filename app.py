from recognizer import Recognition
from speech import Robot

speech = Recognition() # default : Recognition()
robot = Robot()

print("say something!")
speech.listen() # or speech.listen("src/english.wav")
speech.recognize()

print(speech.getText()) # speech.getText("split") for array
robot.speak(speech.getText())
