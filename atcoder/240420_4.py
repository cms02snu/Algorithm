n,a,x,y = map(int,input().split())

db = {}

def f(k):
    global db
    if k==0:
        return 0
    
    if k in db:
        return db[k]
    
    db[k] =  min( f(k//a)+x , f(k//2)/5  + f(k//3)/5 + f(k//4)/5 + f(k//5)/5 + f(k//6)/5 + 6*y/5 )

    return db[k]

print(f(n))