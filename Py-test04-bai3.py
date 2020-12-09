n,m = input().split()
list = []
_max = 0
for i in range(0,int(n),1):
    _str = ''
    a = [int(i) for i in input().split()]
    if _max < max(a):
        _max = max(a)

        
print(_max)
