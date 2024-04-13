# 18109

'''
초성,중성은 반드시 있어야됨
모음을 기준으로 한 글자를 구분해야 할듯
각 글자만 구분할 수 있다면 도깨비불 현상 횟수 세는건 쉬움
받침으로 들어갈 수 없는 자음 있나 확인 - ㄸ,ㅃ,ㅉ

모음과 모음 사이에 자음뭉치가 들어와. 그럼 그 자음을 적당히 초성과 종성으로 
구분할 수 있어야 돼
먼저 다음글자 초성에 자음분배하고 남은걸 전글자 종성으로 넘겨
초성에는 한 알파벳밖에 못들어가
temp에 있는 자음뭉치 중 마지막거를 초성에 나머지를 종성에 넣어

이렇게 글자 나누고 도깨비불 현상 횟수 세
도깨비불 현상 발생 조건 : 
띄어쓰기 없고 앞글자 받침이 없고 뒷글자 자음이 ㄸ,ㅃ,ㅉ가 아님

word : 글자별 알파벳을 담은 리스트
temp : 모음과 모음 사이에 들어갈 종성 및 초성으로 이루어진 자음뭉치 문자열
'''

import sys
input = lambda : sys.stdin.readline().rstrip()

db0 = {'r','R','s','e','E','f','a','q','Q','t','T','d','w','W','c','z','x','v','g'}
db1 = {'k','o','i','O','j','p','u','P','h','hk','ho','hl','y','n','nj','np','nl','b','m','ml','l'}
db2 = {'r','R','rt','s','sw','sg','e','f','fr','fa','fq','ft','fx','fv','fg','a','q','qt','t','T','d','w','c','z','x','v','g'}
db3 = {'rt','sw','sg','fr','fa','fq','ft','fx','fv','fg','qt'}

def solution(S):
    n = len(S)
    word = []
    temp = ''

    for i,a in enumerate(S):
        if not word:
            if a!=' ':
                word.append(a)
            continue

        if len(word[0])==1:
            word[0] += a
            continue

        if a==' ':
            if temp:
                word[-1] += temp
                temp = ''
            word.append('')
            continue

        if a in db1:
            if not temp:
                word[-1] += a
            else:
                word.append(temp[-1])
                word[-2] += temp[:-1]
                temp = ''
                word[-1] += a
        else:
            if i==n-1:
                word[-1] += a
            else:
                temp += a

    count = 0

    for i in range(len(word)-1):
        if word[i] and word[i+1]:
            if (word[i][-1] in db1 and word[i+1][0] in db2) or (word[i][-1]+word[i+1][0] in db3 and word[i][-2] in db1):
                count += 1

    return count

S = input()
print(solution(S))