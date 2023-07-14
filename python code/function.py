'''def display():
    print("hello word")
    print("wellcome")

display()'''

# pass argument

'''def display(a,b):
    print("a :",a)
    print("b :",b)

display(10,30)
display(90,50)'''


'''def sum(a,b):
    s=a+b
    print("sum =",s)

sum(10,30)'''


# print in main program

'''def sum(a,b):
    s=a+b
    return s
 

s=sum(10,30)

print("sum =",s)'''



'''def num_even(a):
    if a%2==0:
        print("number is even")
    else:
         print("number is odd")

num_even(10)'''


#defalt parameter
'''def sum(a=7,b=20):
    s=a+b
    print("sum =",s)

sum()


def sum(a,b=20):
    s=a+b
    print("sum =",s)

sum(8 )'''
 

 
'''def num(a,b,c):
    print(a)
    print(b)
    print(c)

num(8,4,6 )'''



'''def num(a,b,c):
    print(a)
    print(b)
    print(c)

num(c=8,a=4,b=6 )'''

# arbitry agument

'''def num(*abc):
    print(abc)

num(8,4,6,5,6,7,8 )'''


'''def num(*a):
    print(a[0:3])

num(8,4,6,5,6,7,8 )'''

# normal arbbitry argu

def num(c,d,*a):
    print(c)
    print(d)
    print(a)

num(8,4,6,5,6,7,8 )