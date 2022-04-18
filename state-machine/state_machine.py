class State_Machine(object):
    def __init__(self):
        self.state = 'start'
        self.state_set = {
            'start':['start', 'two_1'],
            'two_1':['zero_1', 'two_1'],
            'zero_1':['start', 'two_2'],    
            'two_2':['zero_2', 'two_1'], 
            'zero_2':['start', 'two_1']
        }
        
    def get_col(c):
        if c == '0':
            return 0
        elif c == '2':
            return 1

    def get(self, col):
        pass
