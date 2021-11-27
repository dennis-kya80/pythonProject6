def break_loop():
    for i in range(1,5):
        if(i == 2):
            return(i)
        print(i)
    return

def break_all():
    for j in range(1 ,5):
        for i in range(1, 4):
            if i*j == 6:
                return(i)
            print(i*j)
for i in [0 ,1 ,2 ,3 ,4  ,5]:
    print(i)

for i in range (1, 6):
    print(i)
else:
    print("done")

i = 0
while i < 3:
    print(i)
    i +=1
else:
    print("right")

for i in range(2):
    print(i)
    if i == 1:
        break
else:
    print("done")

a = [1,2,3,4,5]
for i in a:
    if type(i)is not int:
        print(i)
        break
else:
    print("no exception")

a = 10
while True:
    a = a-1
    print(a)
    if a<7:
        break
print("done")
i = 0
while i < 4:
    i +=1