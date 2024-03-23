# 17779

'''
(x,y) 기준 
x+d1+d2가 n 미만
y-d1이 0 이상, y+d2가 n 미만
'''

def divide(x,y):
    result = []
    t = n-1-x
    for d1 in range(1,t):
        for d2 in range(1,t-d1+1):
            if y-d1>=0 and y+d2<n:
                result.append((x,y,d1,d2))

    return result

def distribute(graph,x,y,d1,d2):
    # 5번 선거구
    for i in range(d1+1):
        graph[x+i][y-i] = 5
        graph[x+d2+i][y+d2-i] = 5
    for i in range(d2+1):
        graph[x+i][y+i] = 5
        graph[x+d1+i][y-d1+i] = 5
    
    for i in range(x+1,x+d1+d2):
        start = False
        for j in range(n):
            if graph[i][j]==5:
                if not start:
                    start = True
                else:
                    break
            else:
                if start:
                    graph[i][j] = 5

    # 1번 선거구
    for i in range(x+d1):
        for j in range(y+1):
            if graph[i][j]==0:
                graph[i][j] = 1

    # 2번 선거구
    for i in range(x+d2+1):
        for j in range(y+1,n):
            if graph[i][j]==0:
                graph[i][j] = 2
    
    # 3번 선거구
    for i in range(x+d1,n):
        for j in range(y-d1+d2):
            if graph[i][j]==0:
                graph[i][j] = 3            
    
    # 4번 선거구
    for i in range(x+d2+1,n):
        for j in range(y-d1+d2,n):
            if graph[i][j]==0:
                graph[i][j] = 4

    return graph  

def diff(graph,people):
    population = [-1,0,0,0,0,0]
    for i in range(n):
        for j in range(n):
            population[graph[i][j]] += people[i][j]

    result = max(population[1:]) - min(population[1:])

    return result

def solution(people):
    ways = []
    for i in range(n):
        for j in range(n):
            ways += divide(i,j)

    min_diff = int(1e9)    
    for x,y,d1,d2 in ways:
        temp = [[0]*n for _ in range(n)]
        temp = distribute(temp,x,y,d1,d2)
        min_diff = min(min_diff,diff(temp,people))
    
    return min_diff

'''n = int(input())
people = []
for _ in range(n):
    people.append(list(map(int,input().split())))'''

n = 6
people = [
    [1,2,3,4,1,6],
    [7,8,9,1,4,2],
    [2,3,4,1,1,3],
    [6,6,6,6,9,4],
    [9,1,9,1,9,5],
    [1,1,1,1,9,9]
]
t = [[0]*n for _ in range(n)]
print(distribute(t,2,2,1,1))

print(solution(people))