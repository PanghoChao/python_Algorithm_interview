#Input: 
grid1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
# Output: 1

#Input: 
grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
# Output: 3

        

def numIslands(grid: list[list[str]]) -> int:
    #예외처리 
    if not grid:
        return 0


    cnt = 0 #섬의 갯수 

    for i in range(len(grid)):
        for j in range(len(grid[0])) :
            if grid[i][j] == '1': #땅인 경우
                dfs(grid, i, j)
                cnt += 1

    return cnt

def dfs(grid, i, j):
    #더이상 땅이 아닌경우 종료
    if i < 0 or i >= len(grid) or\
         j< 0 or j >= len(grid[0]) or\
        grid[i][j] != '1' :
        return 
    # 땅인 경우
    else:
        grid[i][j] = '0'

        # 동서남북 탐색 
        dfs(grid,i+1,j) #아래 (남)
        dfs(grid,i,j+1) #오른쪽 (동)
        dfs(grid,i-1,j) #위(북)
        dfs(grid,i,j-1) #왼쪽 (서)

print(numIslands(grid1))
print(numIslands(grid2))
