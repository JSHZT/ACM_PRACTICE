INT_MAX = 2 ** 31 -1
INT_MIN = -2 ** 31


class Solution(object):
    def myAtoi(self, s):
        ret = StateMachine()
        for i in s:
            ret.get(i)
        return ret.signed * ret.ans
    

class StateMachine():
    def __init__(self):
        self.ans = 0
        self.signed = 1
        self.state = 'start'
        self.state_set = {
            'start':['start', 'signed', 'in_number', 'end'],
            'signed':['end', 'end', 'in_number', 'end'],
            'in_number':['end', 'end', 'in_number', 'end'],
            'end':['end', 'end', 'end', 'end']
        }
    
    def get_col(self, char):
        if char.isspace():
            return 0
        if char == '+' or char == '-':
            return 1
        if char.isdigit():
            return 2
        return 3
    
    def get(self, char):
        self.state = self.state_set[self.state][self.get_col(char)]
        if self.state is 'signed':
            self.signed = -1 if char == '-' else 1
        elif self.state is 'in_number':
            self.ans = self.ans * 10 + int(char)
            self.ans = min(self.ans, -INT_MIN) if self.signed is -1 else min(self.ans, INT_MAX)