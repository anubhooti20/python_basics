import random
# both included
n=random.randint(2,8) 
print(n)

#last one excluded
n1= random.randrange(2,4)
print(n1)

# randomly select one element
l=[10,20,30,40]
n2=random.choice(l)
print(n2)

# random float no between 0 to 1
r= random.random()
print(r)

# take sequence and return sequence btw two given parameters
l1=[10,20,30,40]
random.shuffle(l1)
print(l1)

# random float number between two given parameters
u=random.uniform(3,9)
print(u)