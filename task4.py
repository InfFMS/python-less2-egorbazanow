n = int(input())
i = 0
k = 0
for i in range(1, n+1):
    k = 2**i
    i = i+1
    print(k)