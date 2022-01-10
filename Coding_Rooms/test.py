t = int(input())
a = []
while t>0:
    a.extend(input().split())
    t-=1

b = []
temp = list(set(a))

for i in temp:
    b.append([i, a.count(i)])
    temp.remove(i)

# b = sorted(b)
# for i in b:
#     print(i)