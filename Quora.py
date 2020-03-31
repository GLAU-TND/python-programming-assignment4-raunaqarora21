##Input-->'a',1  'a',3 'a',5 'b',2  'b',6 'c',1 'c',2 'c',3 'c',4 'c',5 'd',4 'd',5 'd',6  'd',7 'e',1 'e',3 'e',5 'e',6



l=list(map(eval,input().split()))
k=int(input())
l1=[]
l2=[]
l3=[]
l4=[]
l5=[]
l6=[]

a,b=l[-1]

for i in range(97,ord(a)+1):
    for j in range(len(l)):
        if l[j][0]==chr(i):
            l1.append(l[j][1])
    l2.append(l1)
    l1=[]

for i in range(len(l2)):
    for j in range(i+1,len(l2)):
        l3.append((chr(i+97),chr(j+97)))
        for z in range(len(l2[i])):
            if l2[i][z] in l2[j]:
                
                l3.append(l2[i][z])
        l4.append(l3)
        l3=[]
                

l4.sort(key=len,reverse=True)

max_length=len(l4[0])

for i in l4:
    if len(i)==max_length:
        l5.append(i)

def apna_fun(lst):
    a,b=lst[0]
    d=max(len(l2[ord(a)-97]),len(l2[ord(b)-97]))
    return(d-len(lst)+1)
l5.sort(key=apna_fun)

for i in range(k):
    l6.append(l5[i][0])
print(l6)
    
    
