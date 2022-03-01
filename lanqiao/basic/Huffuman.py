class Solution(object):
    def Huffman(self, list1):
        cost = []
        while len(list1) != 1:
            sums = temp = 0
            for i in range(2):
                temp = min(list1)
                sums += temp
                list1.remove(min(list1))
            list1.append(sums) 
            cost.append(sums)
        return sum(cost)
    
while True:
    try:
        n = (input())
        l = list(map(int, input().split()))
        result = Solution().Huffman(l)
        print(result)
    except:
        break