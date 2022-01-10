def Knight(a,b):
    if (abs(a[0]-b[0])==2 and abs(a[1]-b[1])==1) or (abs(a[0]-b[0])==1 and abs(a[1]-b[1])==2):
        return 1
    else:
        return 0

a = []
a.append(int(input()))
a.append(int(input()))
b = []
b.append(int(input()))
b.append(int(input()))
if Knight(a,b):
    print("YES")
else:
    print("NO")