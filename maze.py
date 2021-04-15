def printMaze(maze):
    for i in maze:
            print ("\t",i)

def solvemaze(r, c):
   
    #destination (maze[n-1][n-1])
    if (r==n-1) and (c==n-1):
        solution[r][c] = 1
        return True
    
    if r>=0 and c>=0 and r<n and c<n and solution[r][c] == 0 and maze[r][c] == 0:
       
        solution[r][c] = 1
        
        # down
        if solvemaze(r+1, c):
            return True
        
        # right
        if solvemaze(r, c+1):
            return True
        
        # up
        if solvemaze(r-1, c):
            return True
        
        # left
        if solvemaze(r, c-1):
            return True
        
        #backtracking
        solution[r][c] = 0
        
        return False;
    
    return 0;
if __name__ == "__main__":
    n = 5

    # me cung 
    # 1 la o bi chan
    # 0 la duong di
    maze = [
        [0,1,0,1,1],
        [0,0,1,0,0],
        [1,0,1,0,1],
        [0,0,0,1,0],
        [1,1,0,0,0]
    ]

    solution = [[0]*n for _ in range(n)]

    print("Me cung: 1 - o bi chan, 0 - o duoc di chuyen")
    printMaze(maze)

    print("Duong di trong me cung:")

    if(solvemaze(0,0)):
        print("\tVi tri so 1 la duong di den dich")
        printMaze(solution)
    else:
        print ("\tKhong co duong di")