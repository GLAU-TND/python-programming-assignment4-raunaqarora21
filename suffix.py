s=list(map(str,input().split(',')))
l=[]

sf='s'
for i in s:
    if i.startswith(sf):
        l.append(i)
print(l)
        
