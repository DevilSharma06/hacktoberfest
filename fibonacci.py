num=int(input("Enter the number of terms to be generated "))
a=0
b=1
fib=0
i=1
x=num-2
print(a," ")
print(b," ")
while(i<=x):
    fib=a+b
    print(fib," ")
    a=b
    b=fib
    i=i+1
