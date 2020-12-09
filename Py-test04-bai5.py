n = int(input())
list = []
for i in range(0,int(n),1):
    _str = ''
    a = [int(i) for i in input().split()]
    list.append(a)
_list = []
kq = ''
for i in range (0,int(n)):
    for j in range (0,int(n)):
        kq += str(list[j][i]) +' '
        if(j+1==int(n)):
            kq+= '\n'
    
print(kq[:-1])
        
            
    
