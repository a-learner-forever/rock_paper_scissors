import random

pc = "nothing"
cc = 0
c = "nothing"

print("Let us play RPS game.... ")
cc = random.randint(1,3)
if cc==1:
    c = "rock"
elif cc==2:
    c="paper"
else:
    c="scissors"

pc = input("plz enter rock, paper or scissors:")
print('computer chose',c)

if c=="rock":
    if pc=="rock":
        print('It is a tie')
    elif pc=="paper":
        print("player wins!!")
    else :
        print("computer wins!!")

if c=="paper":
    if pc=="rock":
        print('Computer wins')
    elif pc=="paper":
        print("TIE")
    else :
        print("player wins!!")

if c=="scissors":
    if pc=="rock":
        print('player wins')
    elif pc=="paper":
        print("computer wins!!")
    else :
        print("TIE")





   







