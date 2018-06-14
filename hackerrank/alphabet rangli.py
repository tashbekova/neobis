N = map(int(input()))
a = input("input character")
b = input("input character")

for i in range(1,N,2): 
    print((a * (i)).center(N, "-"))
print(a.center(N, "-"))
for i in range(N-2,-1,-2): 
    print(("b" * (i)).center(N, "-"))
