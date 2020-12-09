n,m = input().split()
list = []
for i in range(0,int(n),1):
    _str = ''
    a = [int(i) for i in input().split()]
    _str = str(i) +' '+str(max(a))
    print(_str)
