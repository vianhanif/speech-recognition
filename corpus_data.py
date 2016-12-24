
class CorpusData:
    robot = None
    corpus = []

    def __init__(self, robot):
        self.robot = robot
        self.corpus = [
            # asking robot name
            [
                [
                    "What is your name?",
                    "your name",
                    "How do I",
                    "What should I call you?",
                    "have any name"
                ],
                [
                    "I used to be called as %s" % (self.robot.get_name()),
                    "You can call me %s" % (self.robot.get_name())
                ],
            ],
            # acknowledge user name
            [
                [
                    "My name is",
                    "My friends used to call me"
                ],
                [
                    "Nice to meet you",
                    "Hi, there"
                ]
            ],
        ]

    def getCorpus(self):
        return self.corpus
