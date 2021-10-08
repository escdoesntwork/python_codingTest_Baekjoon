a = list(map(int, input()))
v = 0

while True:
    a.append(a[0]+a[1])
    del a[0]
    print(a)

    if(a[1] > 10):
        a[1] - 10
        a.append(a[0]+a[1])
        del a[0]

    v = v+1

    if(v == 5):
        break
    
