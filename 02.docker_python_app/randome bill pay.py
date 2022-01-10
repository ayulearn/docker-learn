import random
test_seed = int(input("create a seed number: "))
random.seed(test_seed)
na =input("give everybody name seprated by comma ")
n = na.split(", ")
x =len(n)
y = random.randint(0,x-1)
z = n[y]
print(f"{z} is going to pay bill")