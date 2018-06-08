if __name__ == '__main__':
  n = int(input())
scores = []
for _ in range(n):
    name = input()
    grade = float(input())
    scores.append([name, grade])
    
givengrades = sorted({x[1] for x in scores})
sts = sorted(x[0] for x in scores if x[1]==givengrades[1])
for s in sts:
    print(s)
