class Permutations(object):

    def is_permutation(self, str1, str2):
        if str1 is None or str2 is None:
            return False
        str1 = str(list(str1).sort())
        str2 = str(list(str2).sort())    
        return str1 == str2
    
if __name__ == "__main__":
    str1 = 'hzt'
    str2 = 'tzh'
    print(Permutations().is_permutation(str1, str2))