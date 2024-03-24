# 1991

def preorder(a):
    b,c = data[a]
    if b!='.' and c!='.':
        return a + preorder(b) + preorder(c)
    elif b=='.' and c=='.':
        return a
    elif b=='.':
        return a + preorder(c)
    else:
        return a + preorder(b)
    
def inorder(a):
    b,c = data[a]
    if b!='.' and c!='.':
        return inorder(b) + a + inorder(c)
    elif b=='.' and c=='.':
        return a
    elif b=='.':
        return a + inorder(c)
    else:
        return inorder(b) + a
    
def postorder(a):
    b,c = data[a]
    if b!='.' and c!='.':
        return postorder(b) + postorder(c) + a
    elif b=='.' and c=='.':
        return a
    elif b=='.':
        return postorder(c) + a
    else:
        return postorder(b) + a

n = int(input())
data = {}
for _ in range(n):
    a,b,c = input().split()
    data[a] = (b,c)

print(preorder('A'))
print(inorder('A'))
print(postorder('A'))