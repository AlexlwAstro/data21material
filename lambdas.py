def addition(n1,n2):
    return n1 + n2


add = lambda n1, n2: n1 + n2

print(addition(2, 3))
print(add(2, 3))
print(add(2, 4))

savings = [234, 555, 674, 78]
bonus = []

for i in range(len(savings)):
    bonus.append(savings[i]*1.1)

output = map(lambda x: x*1.1, savings)

print(bonus)
print(list(output))
