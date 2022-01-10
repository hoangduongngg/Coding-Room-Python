def Queen(a,b):
    if Rock(a,b)==1 or Bishop(a,b)==1:
        return 1
    else:
        return 0
def Rock(a,b):
    if abs(a[0]-b[0])==0 or abs(a[1]-b[1])==0:
        return 1
    else:
        return 0
def Bishop(a,b):
    if abs(a[0]-b[0]) == abs(a[1]-b[1]):
        return 1
    else:
        return 0

a = []
a.append(int(input()))
a.append(int(input()))
b = []
b.append(int(input()))
b.append(int(input()))
if Queen(a,b):
    print("YES")
else:
    print("NO")