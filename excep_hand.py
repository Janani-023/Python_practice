#nameerror
'''try:
    a=10
    print(b)
except Exception as e:
    print(e)

finally:
    c=90
    print(c)
#arithmetic error or zerodivision error
a=10
b=0
print(a/b)

#Type error
age="25"
print(age+5)
#value error
n=int("janani")
print(n)

#index error
a=[10,20]
print(a[8])

#keyerror
s={"name":"ben"}
print(s["age"])

#filenotfounderror
open("aertry.txt",'r')

#modulenotfound error
import jayanth

#stackoverflow error
import math
print(math.exp(1000))

#memory error
h=[1]*(10**20)
print(h)

try:
    a=int(input("enter a num"))
    b=int(input('enter a num')) 
    if b==0:
        raise Exception('zero tharadhinga')
    c=a+b 
    d=a-b
    e=a/b
    print(c,d,e)
except Exception as e:
    print(e)



balance=int(input("enter your balance"))
assert balance>0,"balance should be greater than 0"
print("transaction ....")'''

def test_flow():
    try:
        return "From Try"
    finally:
        return "From Finally"
print(test_flow())


try:
    num = int("abc")
except Exception:
    print("Generic Catch")
except ValueError:
    print("Specific Catch")







