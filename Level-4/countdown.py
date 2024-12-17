input()
arr = map(int, input().split())
v = int(input())
print(sum([1 for i in arr if i==v]))