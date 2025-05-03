while True:
    try:
        PV = float(input("Enter the initial principle:"))

        if PV <= 0:
            print("Enter + number ")
            continue

        break

    except ValueError:
           print("Enter a number")
                  
while True:
    try:

        R = float(input("Enter the interest rate:"))/100/12
        if R <= 0:
            print("Enter + number ")
            continue

        break

    except ValueError:
           print("Enter a number")
while True:
    try:

        M = float(input("How many time per year is the interest compound:"))
        if M <= 0:
            print("Enter + number ")
            continue

        break

    except ValueError:
           print("Enter a number")

while True:
    try:

        G = float(input("What is the Goal:"))
        if G < 0:
            print("Enter + number ")
            continue

        break

    except ValueError:
           print("Enter a number")
i = 0
UI = PV 


while i < 12:
     UI += UI * R
     i += 1
     print(f"Month {i} Update Interest Rate: {UI:,.2f}")

if G > 0:
     
    i = 0
    UI = PV 


    while UI <= G:
         UI += UI * R
         i += 1
    print(f"It Will Take {i} Months Until Reach the Goal {G:,.2f}")          
