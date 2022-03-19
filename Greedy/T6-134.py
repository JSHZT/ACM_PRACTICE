class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1
        leng = len(gas)
        temp = [0] * leng
        start = 0
        cur = 0
        for i in range(leng):
            temp[i] = gas[i] - cost[i]
            cur += temp[i]
            if cur < 0:
                cur = 0
                start = i + 1
        if cur<0:
            return -1
        return start