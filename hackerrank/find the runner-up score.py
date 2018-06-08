if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    l= list(arr)
    a = max (l)
while max(l)==a:
    l.remove(a)
print (max(l))
