import sys
a = int(input())

for i in range(a):
    i,b = map(int,sys.stdin.readline().split())
    print(i+b)
