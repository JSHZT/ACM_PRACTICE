class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        lens = len(ratings)
        suga = [1] * lens
        for i in range(1, lens):
            if ratings[i-1] < ratings[i]:
                suga[i] = suga[i-1] + 1
        for i in range(lens-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                suga[i] = max(suga[i+1] + 1, suga[i])
        return suga
    
if __name__ == '__main__':
    
    ratings = [1, 0, 2]
    ans = Solution().candy(ratings)
    print(ans)