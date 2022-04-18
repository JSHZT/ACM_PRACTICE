state_set = {
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

def dfs(state, i, j):
    temp = 0
    if i > m or j > n:
        return 0
    new_state = state_set[state][get_col(maps[i][j])]
    if new_state == 'zero_2':
        temp += 1
    return dfs(new_state, i+1, j+1) + dfs(new_state, i+1, j) + dfs(new_state, i, j+1) + temp


m, n = 20, 20
maps = []
if __name__  == "__main__":
    
    with open('test.txt', "r") as fp:
        for line in fp.readlines():
            line.strip('\n')
            line_list = list(line)
            maps.append(line_list)
    m = len(maps)
    n = len(maps[0])
    ans = dfs('start', 0, 0)
    print(ans)