import random

# My Solution 
friends=['Alice','Gloria','AC','Rubi']
random=random.randint(0,len(friends)-1)
print(friends[random])

# Option 1
print(random.choice(friends))

