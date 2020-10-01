arr = input('enter 15 numbers separated by space:')
a=list(map(int, arr.split()))
n = len(a)
t=[]
b = list(map(int, arr.split()))
for x in range(n - 1):
    for y in range(n - x - 1):
        if b[y] < b[y + 1]:
            b[y], b[y + 1] = b[y + 1], b[y]

print('sorted list:',b)
print('a:',a)
for x in b:
    t.append(a.index(x))
print('sorted indices:',t)









