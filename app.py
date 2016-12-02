from recognizer import Recognition
from speech import Robot
from datas import DataSet

speech = Recognition("google") # default : Recognition()
robot = Robot()
data = DataSet("src/dataset.txt")

def saveRecord():
    for word in speech.getText().split():
        data.write(word)
    data.save()

def main():
    speech.listen() # or speech.listen("src/english.wav")
    if speech.recognize():
        #robot.speak("It's me!! I'm Alvian. age 20 years old, still young")
        saveRecord()
        data.toString()
        
if __name__ == '__main__':main()
