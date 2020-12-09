n,m = input().split()
list = []
tong = 0
for i in range(0,int(n),1):
    a = [int(i) for i in input().split()]
    tong = tong + sum(a)
    
print(tong)
