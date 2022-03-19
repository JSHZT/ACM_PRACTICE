class Solution:
    def reconstructQueue(self, people):

        people.sort(key=lambda x: (-x[0], x[1]))
        que = []
	
        for p in people:
            que.insert(p[1], p)
        return que