#This helps in making our code compact
#LIST COMPREHENSION

l=[i for i in range(0,100) if i%2==0]
print(l)

P=[i if i%2==0 else 'not even' for i in range(0,100) ]
print(P)
