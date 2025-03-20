a = 1
print(a)
a+=1
print(a)
a+=1
print(a)
a+=1
print(a)

a = 1
while a < 10:
    a += 1
    print(a)

for i in [0,1,2,3,4]:
    print(i+6)
print("=============")

for i in range(5):
    print(i+6)

for i in range(3):
    for j in range(3):
        print(i,j)

#loop control statements
print("=======")
for i in range(5):
    if i == 2:
        break
    print(i)

print("=======")
for i in range(5):
    if i == 2:
        continue
    print(i)

print("=======")
for i in range(5):
    if i == 2:
        pass
    print(i)
print("=====")
for c in "string":
    print(c)
print("=====")
for key, value in {"a":1, "b":2, "c":3}.items():
    print(key, value)
