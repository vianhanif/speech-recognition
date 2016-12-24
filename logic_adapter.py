from __future__ import unicode_literals
from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement
import random


class ChatAdapter(LogicAdapter):
    def __init__(self, *args, **kwargs):
        super(ChatAdapter, self).__init__(*args, **kwargs)

    def can_process(self, statement):
        return (self.chatbot.storage.count() > 0)

    def process(self, statement):
        responses = self.chatbot.storage.get_random()
        selected_statement = responses.text
        taken_statement = ""
        if "my name is" in statement.text:
                taken_statement = "my name is"
        if "my friend used to call me" in statement.text:
                taken_statement = "my friend used to call me"
        if (taken_statement in statement.text):
                selected_statement = statement.text[len(taken_statement):]
        return 1, Statement(selected_statement) 
