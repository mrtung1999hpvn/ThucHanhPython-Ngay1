import random
KetQua=''
f = open('matran.txt', 'r')
matran = f.read().split('\n')
n = int(matran[0].split(' ')[0]) #Hang
m = int(matran[0].split(' ')[1]) #Cot
print(f'Hang {n}')
print(f'Cot {m}')
matran.pop(0)
_list = []
for i in range (n):
  _list.append(sorted([int(matran[i].split(' ')[j]) for j in range (m)]))
print(_list)
#print(_list)
