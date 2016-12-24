from __future__ import unicode_literals
from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement
import random

class BasicConversation(LogicAdapter):
    test = ""
    
    def __init__(self, arg="asd", *args, **kwargs):
        super(BasicConversation, self).__init__(*args, **kwargs)
        self.test = arg
        print(self.test)

    def can_process(self, statement):
        return ("my name is" in statement.text)

    def process(self, statement):
        return 1, Statement("Hello %s" % (statement.text[len("my name is"):]))
