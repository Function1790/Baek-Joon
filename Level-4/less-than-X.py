_, x = map(int, input().split())
arr = map(int, input().split())
print(" ".join([str(i) for i in arr if i<x]))