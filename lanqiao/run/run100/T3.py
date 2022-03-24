class Rotation(object):

    def is_substring(self, s1, s2):
        return s2 in s1

    def is_rotation(self, s1, s2):
        if s1 is None or s2 is None or len(s1)!=len(s2):
            return False
        return self.is_substring(s1+s1, s2)
    
