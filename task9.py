#multiplies x with y argument
s=lambda x,y: x*y
print( s(5,6))

#fibonacci series
def fib(n):
    r=[0,1]
    any(map(lambda _:r.append(r[-1]+r[-2]),range(2,n)))
    print(r)
n=int(input("Enter number::"))
fib(n)

#multiply list with a number
l=[1,2,3,4,5]
m=list(map(lambda a:a*3,l))
print(m)

#divisible by 9 from the list
l=list(range(1,11))
m=list(filter(lambda a:a%9==0,l))
print(m)

#divisible by 2
l=list(range(2,11))
m=list(filter(lambda a:a%2==0,l))
print(m)

