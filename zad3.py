import getpass
from random import randint

rounds = 0
ai = False
aname = "Josh"
ahand = ""
ascore: int = 0
bname = "Daniel"
bhand = ""
bscore: int = 0
board = ""
while True:
    choice: str = getpass.getpass("Ile rund?")
    if type(int(choice)) == int:
        rounds = int(choice)
    break
print("good job, masz", rounds, "rund")
while True:
    choice: str = getpass.getpass("Walka z maszyną (AI), czy człowiekiem (MP)?")
    if choice == "AI":
        ai = True
        break
    elif choice == "MP":
        break
print("good job, Walczysz z ", "Ai" if ai else "Z ziomkiem")
choice: str = getpass.getpass("Jak Sie nazywa gracz 1?")
aname = choice
choice: str = getpass.getpass("Jak Sie nazywa gracz 2, lub komputer?")
bname = choice

print(aname, "walczy z ", bname, "przez ", rounds, " rund")

for i in range(1, rounds):
    while True:
        choice: str = getpass.getpass(aname, ":K / P / N ")
        if choice == "K" or choice == "P" or choice == "N":
            break
    ahand = choice
    if ai:
        r = randint(0, 2)
        if r == 0:
            bhand = "K"
        elif r == 1:
            bhand = "P"
        else:
            bhand = "N"
    else:
        while True:
            choice: str = getpass.getpass(bname, ":K / P / N ")
            if choice == "K" or choice == "P" or choice == "N":
                break
        bhand = choice
    if ahand == bhand:
        board += "remis, "
    elif ahand == "K" and bhand == "N" or ahand == "N" and bhand == "P" or ahand == "P" and bhand == "K":
        ascore = +1
        board += "Wygrywa " + aname + " "
    else:
        bscore = +1
        board += "Wygrywa " + bname + " "

print(board)
if ascore == bscore:
    print("remis!")
elif ascore > bscore:
    print(aname, "Wygrywa")
elif ascore < bscore:
    print(bname, "Wygrywa")
