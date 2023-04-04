import numpy as np

def tärning ():
    x = np.random.randint(1, 7)
    return x
f, e, d, c, b, a = 0, 0, 0, 0, 0, 0
singel = 0
par = 0
tripple = 0
fordob = 0
yatzy = 0
tärningslag = []
tärningslag2 = []




def done():
    print (tärningslag2)
    print("single: ", singel, "par:", par, "Trippel: ", tripple, "Fourdouble: ", fordob, "yatzy: ", yatzy)
    
for i in range(5):
    x = tärning()
    tärningslag.append(x)
    if (x == 1):
        print(f"...\n.{x}\n...\n")
        f += 1
    elif (x == 2):
        print(f"...\n.{x}.\n...\n")
        e += 1
    elif (x == 3):
        print(f"...\n.{x}.\n...\n")
        d += 1
    elif (x == 4):
        print(f"...\n.{x}.\n...\n")
        c += 1
    elif (x == 5):
        print(f"...\n.{x}.\n...\n")
        b += 1
    elif (x == 6):
        print(f"...\n.{x}.\n...\n")
        a += 1
        
        
while True:        
    keep = int(input("Write the dice u want to keep 1-5 or write a zero "))
    if keep ==0:
        break
    else:
        tärningslag2.append(tärningslag[keep - 1])

redo = input(print("roll again, by typing yes"))
if redo == "yes":
    for i in range(5 - len(tärningslag2)):
        x = tärning()
        tärningslag.append(x)
        if (x == 1):
            print(f"...\n.{x}\n...\n")
            f += 1
        elif (x == 2):
            print(f"...\n.{x}.\n...\n")
            e += 1
        elif (x == 3):
            print(f"...\n.{x}.\n...\n")
            d += 1
        elif (x == 4):
            print(f"...\n.{x}.\n...\n")
            c += 1
        elif (x == 5):
            print(f"...\n.{x}.\n...\n")
            b += 1
        elif (x == 6):
            print(f"...\n.{x}.\n...\n")
            a += 1
else:
    done()

while True:        
    keep = int(input("Write the dice u want to keep 1-5 or write a zero "))
    if keep ==0:
        done()
        break
    else:
        tärningslag2.append(tärningslag[keep - 1])

redo = print("roll again, by typing yes")
if redo == "yes":
    for i in range(5 - len(tärningslag2)):
        x = tärning()
        tärningslag.append(x)
        if (x == 1):
            print(f"...\n.{x}\n...\n")
            f += 1
        elif (x == 2):
            print(f"...\n.{x}.\n...\n")
            e += 1
        elif (x == 3):
            print(f"...\n.{x}.\n...\n")
            d += 1
        elif (x == 4):
            print(f"...\n.{x}.\n...\n")
            c += 1
        elif (x == 5):
            print(f"...\n.{x}.\n...\n")
            b += 1
        elif (x == 6):
            print(f"...\n.{x}.\n...\n")
            a += 1
    
else:
    done()
        

for var in tärningslag2:
    if var == 1:
        singel += 1
    if var == 2:
        par += 1 
    if var == 3:
        tripple += 1
    if var == 4:
        fordob += 1
    if var == 5:
        yatzy = +1
        

done()
