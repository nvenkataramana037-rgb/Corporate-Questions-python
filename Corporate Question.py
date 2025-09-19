
#Sum of all cubes from n-m
m = int(input("enter starting value"))
n = int(input("enter ending value"))

if m > n:
    print(0)
else:
    total_sum = 0
    for i in range(m, n +1):
        total_sum += i ** 3
    print(total_sum) 

#products of all num from n-m
m = int(input("enter starting value"))
n = int(input("enter ending value"))

if m > n:
    print(0)
else:
    total_sum = 0
    for i in range(m, n +1):
        total_sum += i*i
    print(total_sum) 


#product of all even num from n-m
m = int(input("enter starting value"))
n = int(input("enter ending value"))

if m > n:
    print(0)
else:
    total_sum = 0
    for i in range(m, n +1):
        if (i%2==0):
            total_sum += i * i
    print(total_sum)
    
#product of all odd num from n-m
m = int(input("enter starting value"))
n = int(input("enter ending value"))

if m > n:
    print(0)
else:
    total_sum = 0
    for i in range(m, n +1):
        if (i%2!=0):
            total_sum += i * i

    print(total_sum)

 #factorial
n=int(input("enter A Value"))
sum=1
for i in range(1,n+1):
    sum*=i
print(sum)

