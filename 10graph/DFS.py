# 그래프를 표현하는 방법중 인접행렬과 인접리스트가 있는데
# 인접리스트를 
# 딕셔너리를 입력값으로 해서 DFS를 구현 해보자

graph ={
        1:[2,3,4], 
        2:[5], 
        3:[5],
        4:[], 
        5:[6,7], 
        6:[], 
        7:[3]
    }
def recursive_dfs(v, discovered=[]):
    discovered.append(v)
    for w in graph[v]:
        if not w in discovered:
            discovered = recursive_dfs(w,discovered)
    return discovered

print(recursive_dfs(1))
