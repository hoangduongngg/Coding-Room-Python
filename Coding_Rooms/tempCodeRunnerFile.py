s = input()
n = len(s)-1 - list(reversed(s)).index('h')
for i in range(0, s.index('h')+1):
    print(s[i], end ="")
for i in range(s.index('h')+1,n):
    if s[i]=='h':
        print("H", end = "")
    else:
        print(s[i], end ="")
for i in range(n, len(s)):
    print(s[i], end = "")