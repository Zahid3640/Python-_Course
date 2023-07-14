# one variable create space in memory other variable same value assign in sane place
x=10
y=10

print(x is y)

x=100
y=10

print(x is y)

# reverse of is

x=10
y=10

print(x is not y)


x=100
y=10

print(x is not y)