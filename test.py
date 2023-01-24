a = 10
b = 20
print (a+b)
print(a)
print(b)

x=range(6)
for i in x:
    print(i)
y=10
for l in range(2, y):
    print(l)


n = 10
if n > 2:
    for i in range(2, n):
        if (n % i) == 0:
             print (n, "is not a prime no")
             break
    else:
        print (n, "is a prime no")
else:
    print(n, "is not a prime no")






