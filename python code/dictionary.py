# store key pair value
# no indexcing


'''person={
       "name":"zahid",
       "age":20,
       "gender":"mail"
}

#print(type(person))
#print(person)


print(person["name"])'''

person=dict({ "name":"zahid",
       "age":20,
       "gender":"mail"})
'''print(person)
print(len(person))
print('age' in person)'''

'''pkeys=person.keys()
for x in pkeys:
    print(x)

    
pvalues=person.values()
for x in pvalues:
    print(x)



    # items show value in pair

p=person.items()
for x in p:
    print(x)'''

# add 
'''person["name"]="nawaz"
print(person)

# update
person["country"]="pak"
print(person)'''
'''person.update({"age":40})
print(person)'''
'''person.pop('name')
print(person)'''


for x in person:
    print(x,"=", person[x])