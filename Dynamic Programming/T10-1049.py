class Solution(object):
    def lastStoneWeightII(self, stones):
        temp = sum(stones)
        sum_ = temp>>1
        dp = [0 for _ in range(sum_+1)]
        for i in range(len(stones)):
            for j in range(sum_, stones[i]-1, -1):
                dp[j] = max(dp[j], dp[j-stones[i]] + stones[i])
        ans = abs(temp - 2 * dp[-1])
        return ans
    
    
if __name__ == '__main__':
    stones = [2, 7, 8, 1, 1, 4]
    ans = Solution().lastStoneWeightII(stones)
    print(ans)