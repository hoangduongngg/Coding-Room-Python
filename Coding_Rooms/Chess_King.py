def King(a,b):
    if abs(a[0]-b[0])==1 or abs(a[1]-b[1])==1:
        return 1
    else:
        return 0

a = []
a.append(int(input()))
a.append(int(input()))
b = []
b.append(int(input()))
b.append(int(input()))
if King(a,b):
    print("YES")
else:
    print("NO")