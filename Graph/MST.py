inf = 2**30

class Graph(object):
    def __init__(self, maps):
        self.maps = maps
        self.nodenum = self.get_nodenum()
        self.edgenum = self.get_edgenum()
        
    def get_nodenum(self):
        return len(self.maps)
    
    def get_edgenum(self):
        cnt = 0
        for i in range(self.nodenum):
            for j in range(i):
                if self.maps[i][j] < inf and self.maps[i][j]>0:
                    cnt += 1
        return cnt
    
    def prim(self):
        res = []
        if self.nodenum <= 0 or self.edgenum < self.nodenum-1:
            return res
        select_list = [0]
        waiting_list = [i for i in range(1, self.nodenum)]
        while len(waiting_list) > 0:
            begin, end, minweight = 0, 0, inf
            for i in select_list:
                for j in waiting_list:
                    if self.maps[i][j] < minweight:
                        minweight = self.maps[i][j]
                        begin = i
                        end = j
            select_list.append(end)
            waiting_list.remove(end)
            res.append([begin, end, minweight])
        return res


if __name__ == "__main__":
    pass