def CheckBetween():
    print("Between wich two numbers would you like to check?")
    tussengetal = int(input("Lowest number > "))
    tussengetal2 = int(input("Highest number > "))
    strTussengetal = str(tussengetal)
    strTussengetal2 = str(tussengetal2)

    list1 = list(range(tussengetal, tussengetal2))
    primeList = []

    for i in list1:
        tempList = list(range(2, i))
        loopbreak = False
        for j in tempList:
            som = i / j
            if som.is_integer():
                loopbreak = True


        if loopbreak == False:
            primeList.append(i)

    print("These are the Prime Numbers between " + strTussengetal + " and "+ strTussengetal2 + ": ")
    print(primeList)

def CheckIfPrime():
    getal = int(input("Please enter a number > "))
    strGetal = str(getal)
    print("Your number is: " +strGetal)

    list2 = list(range(2, (getal)))
    loopbreak = False
    isint = False

    deelList = [1]

    for i in list2:
        som = getal / i
        if som.is_integer():
            deelList.append(i)
            loopbreak = True
            isint = True

    deelList.append(getal)

    if loopbreak == False:
        print(strGetal + " is a Prime Number!")

    elif isint and loopbreak:
        print(strGetal + " is not a Prime Number!")
        print("This can be divided by: ")
        print(deelList)

exit = False

line1 = print("Welcome to Prime Checker!")
line2 = print("Here you can check if a specific number is a Prime Number or check for Prime Numbers between two numbers")
line3 = print('Type "help" for more information')

while exit == False:
    userinput = input("> ")

    if userinput == "help":
        print("Type 'between' to check for Prime Numbers between two numbers")
        print("Type 'check' to check if a specific number is a Prime Number")
        print("Type 'exit' to exit")
        print("Type 'help' for help")
        print()
    elif userinput == "between":
        CheckBetween()
    elif userinput == "check":
        CheckIfPrime()
    elif userinput == "exit":
        break
    else:
        print("Input not recognised, try again or type 'help' for more information")
