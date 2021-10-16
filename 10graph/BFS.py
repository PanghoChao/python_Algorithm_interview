# BFS 이다. 
# DFS보다는 적게 쓰인다고 하나, 추후에 최단경로를 찾는 다익스트라 알고리즘에서 사용된다고 한다.
# DFS 와 똑같은 graph를 활용해 구현해보자

#BFS는 반복구조 밖에 없다 (큐 활용)
graph ={
        1:[2,3,4], 
        2:[5], 
        3:[5],
        4:[], 
        5:[6,7], 
        6:[], 
        7:[3]
    }


def iterative_bfs(start_v):
    discovered= []
    queue = [start_v]
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
           if v not in discovered:
                discovered.append(v)
                queue.append(w)
    return discovered

print(iterative_bfs(1))
