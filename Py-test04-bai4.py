n = int(input())
list = []
for i in range(0,int(n),1):
    _str = ''
    a = [int(i) for i in input().split()]
    list.append(a[i])

print(max(list))
