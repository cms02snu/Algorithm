'''
index : i가 현재 몇번째에 있는지 저장
1번부터 1번째 자리로 옮긴다
이미 i가 i번째 자리에 있으면 패스

data[i]와 i와 자리 스왑
data 상에서 순서 교체, index 교체
'''

n = int(input())
data = [-1] + list(map(int,input().split()))

index = [-1] * (n+1)
for i,a in enumerate(data):
    if i==0:
        continue
    index[a] = i

count = 0
result = []

for i in range(1,n+1):
    if i==index[i]:
        continue

    count += 1

    idx = index[i]
    result.append((index[data[i]],index[i]))
    
    index[data[i]],index[i] = index[i],index[data[i]]
    data[i],data[idx] = data[idx],data[i]

print(count)
for a,b in result:
    print(a,b)