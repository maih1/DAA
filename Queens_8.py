def is_attack(i, j):
    # kiểm tra nếu có một quân trong hàng hoặc cột
    for k in range(N):
        if board[i][k] == 1 or board[k][j] == 1:
            return True
    
    # Kiểm tra đường chéo
    for k in range(N):
        for l in range(N):
            if (k + l == i + j) or ( k - l == i - j):
                if board[k][l] == 1:
                    return True
    return False

def N_queen(n):
    
    # Kết quả
    if n == 0:
        return True
    
    for i in range(N):
        for j in range(N):
            
            # Kiểm tra vị trí đặt quân hậu
            if (not(is_attack(i, j))) and (board[i][j] != 1):
                board[i][j] = 1
                
                if N_queen(n-1)==True:
                    return True
                board[i][j] = 0

    return False

if __name__ == "__main__":
    
    # Số quân hâu
    N = 8
    board = [[0]*N for _ in range(N)]

    N_queen(N)
    
    print("Vị trí của {} quân hậu trên bàn cờ - vị trí các số 1".format(N))
    for i in board:
        print (i)