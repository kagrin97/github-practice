def attach(x, y, M, key, board):
    for i in range(M):
        for j in range(M):
            board[x+i][y+j] += key[i][j] # 키를 맞춰봄

def detach(x, y, M, key, board):
    for i in range(M):
        for j in range(M): 
            board[x+i][y+j] -= key[i][j] # 키를 빼줌

def rotate90(arr):
    return list(zip(*arr[::-1])) # *는 언팩킹, zip은 나눠진 리스트를 합쳐줌 

def check(board, M, N):
    for i in range(N):
        for j in range(N):
            if board[M+i][M+j] != 1: # 키가 안들어간곳 
                return False # 실패
    return True # 성공

def solution(key, lock):
    M, N = len(key), len(lock) # 키는 항상 자물쇠보다 작거나 같다

    board = [[0] * (M*2 + N) for _ in range(M*2 + N)] # 중앙에 자물쇠를 넣을 판을 만듦
    for i in range(N):
        for j in range(N):
            board[M+i][M+j] = lock[i][j] # 자물쇠를 중앙에 넣음

    rotated_key = key 
    for _ in range(4):
        rotated_key = rotate90(rotated_key) # 오른쪽으로 돌려줌
        for x in range(1, M+N):
            for y in range(1, M+N): # m+n은 키[0][0]이 자물쇠[-1][-1]이 만나는 지점
                attach(x, y, M, rotated_key, board)
                if(check(board, M, N)): 
                    return True # 키가 다들어갔기때문에 성공
                detach(x, y, M, rotated_key, board) # 키를 빼줌
                
    return False # 모든키를 넣어봐도 실패함

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))


