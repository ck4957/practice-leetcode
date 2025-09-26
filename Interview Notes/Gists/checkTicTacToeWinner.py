board = [[1,-1, 1,1],[1,-1,1,-1],[1,-1,1,-1],[-1,1,-1,0]]
def checkTicTacToe(board):
    #board length
    rows = len(board)
    
    # Horizontal
    X_count = Y_count = 0
    for i in range(rows):
        for j in range(rows):
            if board[i][j]==-1:
                X_count+=1
            elif board[i][j]==1:
                Y_count+=1
        if X_count == rows:
            return -1
        elif Y_count == rows:
            return 1
    
    # Vertical
    X_count = Y_count = 0
    for i in range(rows):
        for j in range(rows):
            if board[j][i]==-1:
                X_count+=1
            elif board[j][i]==1:
                Y_count+=1
        if X_count == rows:
            return -1
        elif Y_count == rows:
            return 1
    
    # Forward Diagonal
    X_count = Y_count = 0
    for i in range(rows):
        if board[i][i]==-1:
            X_count+=1
        elif board[i][i]==1:
            Y_count+=1
        if X_count == rows:
            return -1
        elif Y_count == rows:
            return 1

    # Backward Diagonal
    X_count = Y_count = 0
    for i in range(rows):
        if board[i][rows-1-i]==-1:
            X_count+=1
        elif board[i][rows-1-i]==1:
            Y_count+=1
        if X_count == rows:
            return -1
        elif Y_count == rows:
            return 1

    # Spaces
    for i in range(rows):
        for j in range(rows):
            if board[i][j]==0:
                return 0
                
    # No winner and space 
    return 2

print(checkTicTacToe(board))