# 17615

'''
맨 끝에 무리에 있지 않은 공의 개수
'''

n = int(input())
data = input()

cnt_red_front = 0
cnt_blue_front = 0
cnt_red_back = 0
cnt_blue_back = 0

red = 0
blue = 0
for a in data:
    if a=='R':
        red += 1
    else:
        blue += 1

s = data[0]
start = 0
for a in data:
    if a==s:
        start += 1
    else:
        break

e = data[-1]
end = 0
for a in data[::-1]:
    if a==e:
        end += 1
    else:
        break

if s=='R':
    cnt_red_front = red - start
    cnt_blue_front = blue
else:
    cnt_red_front = red
    cnt_blue_front = blue - start

if e=='R':
    cnt_red_back = red - end
    cnt_blue_back = blue
else:
    cnt_red_back = red
    cnt_blue_back = blue - end

print(min(cnt_red_front,cnt_blue_front,cnt_red_back,cnt_blue_back))