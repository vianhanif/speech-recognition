
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
                    "I am used to be called as %s" % (self.robot.get_name()),
                    "You can call me %s" % (self.robot.get_name()),
                    "I am identified as %s" % (self.robot.get_name()),
                    "though my name could change overtime, but you can call me %s for now" % (self.robot.get_name()),
                    "as you can see the label, my name is %s" % (self.robot.get_name())
                ],
            ],
            # asking about age
            [
                [
                    "how old",
                    "what is your age?"
                ],
                [
                    "I believe i'm young, though i can't say much about that",
                    "how old do you think i am?"
                ]
            ],
            #acknowledge thought
            [
                [
                    "I think",
                    "probably about",
                ],
                [
                    "Thank you for the consideration",
                    "nice thought"
                ]
            ],
            # acknowledge user name
            [
                [
                    "My name is",
                    "used to call me",
                    "call me",
                ],
                [
                    "Nice to meet you",
                    "Hi, there",
                    "Happy to see you",
                ]
            ],
            # acknoledge user age
            [
                [
                    "years old",
                ],
                [
                    "I hope you will stay healthy",
                    "no matter how old, you'll still growing for a better person",
                    "Always happy to see a healthy person at such age",
                    "I expect I can get close with such person now",
                ]
            ],
            [
                [
                    "living in",
                    "live in",
                    "staying in",
                ],
                [
                    "I hope you happiness by living there",
                    "I wish I can see your place",
                    "your home must be looking really nice",
                    "I can never compare mine with such a place",
                ]
            ],
            # acknowledge user job
            [
                [
                    "working as",
                    "work in",
                    "job is",
                    "working in",
                ],
                [
                    "Such an enjoyable job",
                    "Such responsibility must have made you proudful",
                    "your family must be proud of you",
                    "You must be busy",
                    "if I may, I am proud of you",
                    "Such an interesting job",
                ]
            ],
            # ackbowledge user family
            [
                [
                    "living with",
                    "to live with"
                ],
                [
                    "It must be fun living with them",
                    "I hope you happiness living with them",
                    "I wish I could have such family",
                    "How wonderful",
                ]
            ],
            # acknowledge user hobby
            [
                [
                    "I like",
                    "usually play",
                ],
                [
                    "is that your hobby?",
                    "what a fun fact about you",
                    "Such a fun activity",
                ]
            ],
            #responding yes question
            [
                [
                    "yes"
                ],
                [
                    "very well then..",
                    "nice...",
                ]
            ],
            #responding no question
            [
                [
                    "no",
                    "not"
                ],
                [
                    "Okay then..."
                ]
            ],
            [
                [
                    "Thank you",
                    "that's a nice",
                ],
                [
                    "you're welcome"
                ]
            ]
        ]

    def getCorpus(self):
        return self.corpus
