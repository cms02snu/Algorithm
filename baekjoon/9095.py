# 9095

'''
dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
'''

N = int(1e9) + 9

table = [1] * (int(1e6)+1)

for i in range(1,int(1e6)+1):
    if i==1:
        table[1] = 1
    elif i==2:
        table[2] = 2
    else:
        table[i] = table[i-1]+table[i-2]+table[i-3]
        table[i] = table[i]%N

for _ in range(int(input())):
    print(table[int(input())])