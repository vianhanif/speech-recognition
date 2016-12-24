# -*- coding: utf-8 -*-

class CorpusTrainer:
        robot = None
        corpus = []

        def __init__(self, robot, corpus=[]):
                self.robot = robot
                self.corpus = corpus
                self.trains(self.corpus)

        def trains(self, lists):
                for item in lists:
                        for question in item[0]:
                                for answer in item[1]:
                                        self.robot.train(
                                                [str(question).lower(),
                                                 str(answer).lower()])
        
        def train(self, corpus):
                self.robot.train(corpus)
                

        
