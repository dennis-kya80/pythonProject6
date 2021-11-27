def counter():
    num = 0
    def increment():
        nonlocal num
        num +=1
        return num
    return "incrementer"


number = 5

if number > 2:
    print("Number is greater than 2.")
elif number < 2:
    print("Number is smaller than 2.")
else:
    print("Number is 2.")


a = 1
b = 2
if a and b > 2:
    print("yes")
else:
    print("no")

a = "python is fun!"
b = "python is fun!"
print(a is b)

i = 0
while i < 7:
    print(i)
    if i == 4:
        print("Breaking from loop")
        break
    i +=2

for i in (0, 1 ,2 ,3 ,4 ,5 , 6):
    print(i)
    if i == 5:
        break
for i in (0 ,1 ,2 ,3 ,4 ,5 ,6):
    if i == 3 or i ==5:
        continue
    print(i)
while True:
    for i in range(1,5):
        if i == 2:
            break

