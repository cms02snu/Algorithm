# 16235

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

def solution(dnutrient,trees,k):
    graph = [[[] for _ in range(n)] for _ in range(n)]
    for x,y,age in trees:
        graph[x][y].append(age)

    nutrient = [[5]*n for _ in range(n)]

    temp = []

    for _ in range(k):
        # 봄,여름
        for i in range(n):
            for j in range(n):
                plus = 0
                # 양분먹기(사망)
                if len(graph[i][j])==1:
                    if graph[i][j][0]<=nutrient[i][j]:
                        nutrient[i][j] -= graph[i][j][0]
                        graph[i][j][0] += 1
                    else:
                        plus += graph[i][j][0]//2
                        graph[i][j].pop(0)
                elif len(graph[i][j])>1:
                    graph[i][j].sort()
                    while graph[i][j]:
                        age = graph[i][j].pop(0)
                        if age<=nutrient[i][j]:
                            nutrient[i][j] -= age
                            temp.append(age+1)
                        else:
                            plus += age//2
                    while temp:
                        age = temp.pop(0)
                        graph[i][j].append(age)
                # 나이증가
                nutrient[i][j] += plus

        # 가을
        for x in range(n):
            for y in range(n):
                for age in graph[x][y]:
                    if age%5==0:
                        for d in range(8):
                            nx = x + dx[d]
                            ny = y + dy[d]
                            if nx>=0 and nx<n and ny>=0 and ny<n:
                                graph[nx][ny].append(1)

        # 겨울
        for i in range(n):
            for j in range(n):
                nutrient[i][j] += dnutrient[i][j]

    count = 0
    for i in range(n):
        for j in range(n):
            count += len(graph[i][j])

    return count

n,m,k = map(int,input().split())
dnutrient = []
for _ in range(n):
    dnutrient.append(list(map(int,input().split())))
trees = []
for _ in range(m):
    a,b,c = map(int,input().split())
    trees.append((a-1,b-1,c))

print(solution(dnutrient,trees,k))