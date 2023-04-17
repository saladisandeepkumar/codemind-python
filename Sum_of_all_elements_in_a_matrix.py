r,c=map(int,input().split())
mat=[]
s=0
for i in range(r):
    mat=list(map(int,input().split()))
    s+=sum(mat)
print(s)
    