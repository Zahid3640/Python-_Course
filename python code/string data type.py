# singlle line use ""
'''x="zahid"
print(x)


# multile line use """


x="""line 1
line 2
line 3
"""
print(x)

# indexcing in string


x="i love pakistan"
print(x[0])
print(x[1])
print(x[-1])


# length of string

x="i love pakistan"
print(len(x))

# in 

x="i love pakistan"
print('pak' in x)
print('uv' in x)


# not in 

x="i love pakistan"
print('pak' in x)
print('uv' in x)


# slicing of string
# giving starting and ending point end point not included

x="i love pakistan"
print(x[2:9])
print(x[:9])
print(x[2:])



# string concatenation
x='zahid'
y='nawaz'

print(x+" "+y)

# string formating


x='zahid'
y='nawaz'
si="my nane is {1} and father name is {0}"
print(si.format(x,y))'''

# string escaping


x="i love \n \"great\" pakistan"
print(x)


x="i love \n \"great\" pakistan"
print(x)


x="i love \\n \"great\" pakistan"
print(x)


# string method


x="i love pakistan"
print(x.upper())
x="i love pakistan"
print(x.lower())