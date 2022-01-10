#O DEN: CUNG LE OR CUNG CHAN
def Black(a):
    if (a[0]%2==1 and a[1]%2==1) or(a[0]%2==0 and a[1]%2==0):
        return 1
    else:
        return 0
def White(a):
    if Black(a):
        return 0
    else:
        return 1

a = []
a.append(int(input()))
a.append(int(input()))
b = []
b.append(int(input()))
b.append(int(input()))
if Black(a)==Black(b): #cung mau
    print("YES")
else:
    print("NO")