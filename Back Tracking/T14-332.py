from collections import defaultdict
class Solution(object):
    def findItinerary(self, tickets):
        tickets_dict = defaultdict(list)
        path = ["JFK"]
        lens = len(tickets)
        for i in tickets:
            tickets_dict[i[0]].append(i[1])
        
        def backtracking(start_point):
            if len(path) == lens + 1:
                return True
            tickets_dict[start_point].sort()
            for _ in tickets_dict[start_point]:
                endpoint = tickets_dict[start_point].pop(0)
                path.append(endpoint)
                if backtracking(endpoint):
                    return True
                path.pop()
                tickets_dict[start_point].append(endpoint)
        backtracking("JFK")
        return path