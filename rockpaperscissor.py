choice1=input("Player 1 to choose from rock, paper, scissors: ")
choice2=input("Player 2 to choose from rock, paper, scissors: ")
ch1=str.lower(choice1)
ch2=str.lower(choice2)
if (ch1=="rock" and ch2=="scissors"):
    print("Player 1 has won")
    dec=input("Do you want to continue? ")
elif (ch1=="scissors" and ch2=="paper"):
    print("Player 1 has won")
    dec=input("Do you want to continue? ")
elif (ch1=="paper" and ch2=="rock"):
    print("Player 1 has won")
    dec=input("Do you want to continue? ")
elif (ch2=="rock" and ch1=="scissors"):
    print("Player 2 has won")
    dec=input("Do you want to continue? ")
elif (ch2=="scissors" and ch1=="paper"):
    print("Player 2 has won")
    dec=input("Do you want to continue? ")
elif (ch2=="paper" and ch1=="rock"):
    print("Player 2 has won")
    dec=input("Do you want to continue? ")
else:
    print("Error")
deci=str.lower(dec)

while(deci=="yes"):
    choice1=input("Player 1 to choose from rock, paper, scissors: ")
    choice2=input("Player 2 to choose from rock, paper, scissors: ")
    ch1=str.lower(choice1)
    ch2=str.lower(choice2)
    if (ch1=="rock" and ch2=="scissors"):
        print("Player 1 has won")
        dec=input("Do you want to continue? ")
    elif (ch1=="scissors" and ch2=="paper"
        print("Player 1 has won")
        dec=input("Do you want to continue? ")
    elif (ch1=="paper" and ch2=="rock"):
        print("Player 1 has won")
        dec=input("Do you want to continue? ")
    elif (ch2=="rock" and ch1=="scissors"):
        print("Player 2 has won")
        dec=input("Do you want to continue? ")
    elif (ch2=="scissors" and ch1=="paper"):
        print("Player 2 has won")
        dec=input("Do you want to continue? ")
    elif (ch2=="paper" and ch1=="rock"):
        print("Player 2 has won")
        dec=input("Do you want to continue? ")
    else:
        print("Error")
    deci=str.lower(dec)


   
