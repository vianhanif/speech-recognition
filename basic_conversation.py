from __future__ import unicode_literals
from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement
from random import randint

class BasicConversation(LogicAdapter):
    statement_list = []
    note = {}
    callback = {}
    
    def __init__(self, *args, **kwargs):
        super(BasicConversation, self).__init__(*args, **kwargs)

    def set_data(self):
        self.statement_list = [
            {
                'id': 'NAME',
                'prefix': [
                    'name is',
                    'call me'
                ],
                'handler': self._name,
                'feedback': [
                    ('Hello %s'),
                    ('Nice to see you, %s'),
                ],
            },
            {
                'id': 'AGE',
                'prefix': [
                    'i am',
                    "i'm"
                ],
                'postfix': [
                    1,
                    [
                        'year old',
                        'years old',
                    ]
                ],
                'handler': self._age,
                'feedback': [
                    ['such a young age...', 'twenty'],
                    ["i can still see you as a young person!", 'thirty'],
                    ["i hope you'll stay healthy :)", 'fourty'],
                    [
                        "you're still growing...",
                        [
                            'one', 'two', 'three', 'four', 'five',
                            'six', 'seven', 'eight', 'nine', 'ten',
                            'eleven', 'twelve', 'thirteen', 'fourteen',
                            'fifteen', 'sixteen', 'seventeen', 'eighteen',
                            'nineteen'
                        ]
                    ],
                    [('long live %s!')]
                ]
            },
            {
                'id': 'PLACE',
                'prefix': [
                    'live in',
                    'living in',
                    'living at',
                    ' in ',
                ],
                'postfix': [
                    0,
                    [
                        ' for ',
                        ' with ',
                        ' at ',
                    ]
                ],
                'handler': self._place,
                'feedback': [
                    '%s. Such a nice place to stay',
                    ("i hope you're happy living in %s")
                ],
            },
        ]

    def can_process(self, statement):
        self.set_data()
        _process = False
        for item in self.statement_list:
            for prefix in item['prefix']:
                if prefix in statement.text:
                    self.callback = item
                    self.callback['prefix'] = prefix
                    prefix_i = (self.find_str(statement.text, prefix) + len(prefix))
                    self.note[item['id']] = statement.text[(prefix_i):]
                    _process = True
                    if 'postfix' in item:
                        for postfix in item['postfix'][1]:
                            if postfix in statement.text:
                                return _process
                        if item['postfix'][0] == 1:
                            _process = False
                            break
                        else:
                            _process = True
                            break
                    else:
                        break
        return _process

    def process(self, statement):
        response = self.callback['handler'](self.note[self.callback['id']])
        return 1, Statement(response)

    def find_str(self, s, char):
        index = 0
        if char in s:
            c = char[0]
            for ch in s:
                if ch == c:
                    if s[index:index+len(char)] == char:
                        return index
                index += 1
        return -1

    def get_postfix(self, statement):
        for postfix in self.callback['postfix']:
            if postfix in statement:
                return postfix
        return ""

    def _name(self, statement):
        feedbacks = self.callback['feedback']
        self.note[self.callback['id']] = statement
        answer = feedbacks[int(randint(0, (len(feedbacks)-1)))]
        return (answer % (self.note[self.callback['id']]))

    def _age(self, statement):
        feedbacks = self.callback['feedback']
        
        self.note[self.callback['id']] = statement
        for feedback in feedbacks:
            if len(feedback) > 1:
                if isinstance(feedback[1], list):
                    for age in feedback[1]:
                        if age in statement:
                            return feedback[0]
                elif feedback[1] in statement:
                    return feedback[0]
        return (feedbacks[len(feedbacks)-1][0] % (self.note['NAME']))

    def _place(self, statement):
        for postfix in self.callback['postfix'][1]:
            pos = self.find_str(statement, postfix)
            if pos > -1:
                for prefix in self.callback['prefix']:
                    pre = self.find_str(statement, prefix)
                    if pos > pre:
                        self.note[self.callback['id']] = statement[0:pos]
                        break
                    else:
                        self.note[self.callback['id']] = statement[0:pos]
                        break
        feedbacks = self.callback['feedback']
        answer = feedbacks[int(randint(0, (len(feedbacks)-1)))]
        return (answer % (self.note[self.callback['id']]))





    
