a, b = map(int, input().split())
c, d = map(int, input().split())

print(max(a-c, max(a-d, max(b-c, b-d))))
