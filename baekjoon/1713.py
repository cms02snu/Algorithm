# 1713

def solution(n,seq):
    board = []

    for i,a in enumerate(seq):
        exist = False
        for j,(x,y,z) in enumerate(board):
            if z==a:
                board[j] = (x+1,y,z)
                exist = True

        if not exist:
            if len(board)==n:
                board.pop(0)
            board.append((1,i,a))

        board.sort()

    result = [c for a,b,c in board]
    result.sort()
    result = [str(a) for a in result]

    print(' '.join(result))

n = int(input())
k = int(input())
seq = list(map(int,input().split()))

solution(n,seq)