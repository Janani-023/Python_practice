#nested if
'''cutoff=float(input("enter the cutoff"))
c12=int(input("enter the 12th"))
if c12>=60:
    if cutoff>=190:
        print("eligible for \n")
        print("1.CSE")
        print("2.ECE")
        print("3.IT")
        if c12>=90:
            print("scolraship")
    elif cutoff>=170:
        print("1.Mech")
        print("2.EEE")
    else:
        print("you cut ff is low")
        
else:
    print("12th mark too low!!!")'''


#looping control/itervative contro/repetative control
    #for loops
#intergers are not iterable so we use range fun(start,end,step)
for i in range(1,16,2):
    print(i,"hi")
#strng is iterable  
for j in "janani":
    print(j)
    
a=["rithika","sanjay","nimal","jana","ashwin"]
for z in a:
    print(z)
#nested for
for i in range(6):
    for j in range(6):
        print("*",end="")
    print()

for i in range(1,6):
    for j in range(i):
        print("*",end="")
    print()

for i in range(5,0,-1):
    print(i)

for i in range(5,0,-1):
    for j in range(i):
        print("*",end="")
    print()

for i in range(5,0,-1):
    for j in range(i):
        print("*",end="")
    print()



















    
