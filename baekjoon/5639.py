# 5639

'''
dfs 해서 -1을 찾으면 그 자리에 i가 들어가면 된다
root node부터 안으로 들어가는데 기준 node보다 작으면
왼쪽, 크면 오른쪽으로 간다
'''

import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(int(1e4))

def dfs(x,i):
    if i<x:
        if tree[x][0]==-1:
                tree[x][0] = i
                tree[i] = [-1,-1]
        else:
                dfs(tree[x][0],i)
    else:
        if tree[x][1]==-1:
                tree[x][1] = i
                tree[i] = [-1,-1]
        else:
            dfs(tree[x][1],i)

def postorder(x):
    if tree[x]==[-1,-1]:
        _post.append(x)
    elif tree[x][0]==-1:
        postorder(tree[x][1])
        _post.append(x)        
    elif tree[x][1]==-1:
        postorder(tree[x][0])
        _post.append(x)
    else:
        postorder(tree[x][0])
        postorder(tree[x][1])
        _post.append(x)        

def solution(preorder):
    global tree,_post
    root = preorder[0]
    tree = {root:[-1,-1]}
    for i in preorder[1:]:
        dfs(root,i)

    _post = []
    postorder(root)

    for i in _post:
        print(i)

preorder = []
while True:
    a = input()
    if a=='':
        break
    preorder.append(int(a))

solution(preorder)