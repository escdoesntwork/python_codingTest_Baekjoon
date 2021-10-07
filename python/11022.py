a = int(input())

for i in range(a):
    z,x = map(int, input().split())
    print("Case #%d: %d + %d = %d" % (i+1,z,x,z+x))
