'''
이 게임에서 어떤 플레이가 최적의 플레인지 정의해야 함
dp[배열] (a가 둘 차례) : 
a가 어떻게 두든 b가 이길 방법 하나라도 있으면 b 승
특정 경우에서 b승이라면 b 승

dp[배열] = dp[다음배열]
'''

def done(graph):
    # row
    for i in range(3):
        if graph[i][0]==graph[i][1]==graph[i][2] and graph[i][0]!=0:
            if graph[i][0]==1:
                return True,'A'
            else:
                return True,'B'
            
    # col
    for j in range(3):
        if graph[0][j]==graph[1][j]==graph[2][j] and graph[0][j]!=0:
            if graph[0][j]==1:
                return True,'A'
            else:
                return True,'B'
            
    # diag
    if graph[0][0]==graph[1][1]==graph[2][2] and graph[0][0]!=0:
        if graph[0][0]==1:
            return True,'A'
        else:
            return True,'B'
    if graph[0][2]==graph[1][1]==graph[2][0] and graph[0][2]!=0:
        if graph[0][2]==1:
            return True,'A'
        else:
            return True,'B'
        
    zero = 0
    result = 0
        
    for i in range(3):
        for j in range(3):
            if graph[i][j]==1:
                result += data[i][j]
            elif graph[i][j]==0:
                zero += 1
            else:
                result -= data[i][j]

    if zero>0:
        return False,-1
    
    if result>0:
        return True,'A'
    else:
        return True,'B'

def dp(graph):
    _done,winner = done(graph)
    if _done:
        return winner

    _sum = 0
    for i in range(3):
        for j in range(3):
            _sum += graph[i][j]
    
    if _sum==0:
        turn = 'A'
    else:
        turn = 'B'

    br = False
    if turn=='A':
        winner = 'B'
        for i in range(3):
            if br:
                break
            for j in range(3):
                if br:
                    break
                if graph[i][j]==0:
                    graph[i][j] = 1
                    if dp(graph)=='A':
                        winner = 'A'
                        graph[i][j] = 0
                        br = True
                    graph[i][j] = 0
    else:
        winner = 'A'
        for i in range(3):
            if br:
                break
            for j in range(3):
                if br:
                    break
                if graph[i][j]==0:
                    graph[i][j] = -1
                    if dp(graph)=='B':
                        winner = 'B'
                        graph[i][j] = 0
                        br = True
                    graph[i][j] = 0

    return winner

def solution(data):
    result = dp([[0,0,0],[0,0,0],[0,0,0]])

    if result=='A':
        print('Takahashi')
    else:
        print('Aoki')

data = []
for _ in range(3):
    data.append(list(map(int,input().split())))

solution(data)
