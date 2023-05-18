cards = int(input())
s = []
for i in range(1, cards+1):
    s.append(i)
while len(s) > 1:
    print(s.pop(0), end=" ")
    s.append(s.pop(0))
print(s[0])
