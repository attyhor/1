"""
Kö/papír/olló verzió 0.2
fejlesztendő:
- eredmény kiírása fájlba, onnét visszatöltése
- játékos felismerése, statisztika
- két human hálózaton
"""

import random


more_game = {"i", "n"}
possibility = {"k", "p", "o"}

ai_win = {"ko", "op", "pk"}
human_win = {"ok", "po", "kp"}
ai_tipp = ""
human_tipp = ""


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score


def tovabb():
    user_input = input("Szeretnél még játszani (i/n)?: ")
    while user_input not in more_game:
        print("A válasz i vagy n legyen!")
        user_input = input("Szeretnél még játszani (i/n)?: ")
    return user_input


def h_tipp():
    human_tipp = input("Kérem a választásod (kő:k / papír:p / olló:o) :")
    while human_tipp not in possibility:
        print("A válasz k, p vagy o legyen!")
        human_tipp = input("Kérem a választásod (kő:k / papír:p / olló:o) :")
    return human_tipp


def tipp():
    ai_tipp = random.choice(["k", "p", "o"])
    human_tipp = h_tipp()
    print("A gép tippje: {} {} tippje: {}".format(ai_tipp, human.name, human_tipp))
    eredmeny = ai_tipp + human_tipp
    return eredmeny


def whowin(eredmeny):
    if eredmeny in ai_win:
        ai.score += 1
        print("Ezt a menetet a CPU nyerte!")
        return
    elif eredmeny in human_win:
        human.score += 1
        print("Ezt a menetet {} nyerte!".format(human.name))
        return
    else:
        print("Ez döntetlen lett.")
        return


def allas(fordulo):
    print("\nAz állás a {}. forduló után:\n \tCPU: \t{} pont\n\t{}:\t{} pont".format(fordulo, ai.score, human.name, human.score))


def vege():
    if ai.score == 5:
        print("\nA meccset CPU nyerte:\n\tCPU: \t{} pont\n\t{}:\t{} pont".format(ai.score, human.name, human.score))
        ai.score, human.score = 0, 0
        return 0
    elif human.score == 5:
        print("\nA meccset {} nyerte:\n\t{}: \t{} pont\n\tCPU:\t{} pont".format(human.name, human.name, human.score, ai.score))
        ai.score, human.score = 0, 0
        return 0
    else:
        return 1


def main():
    mehet = "i"
    fordulo = 0
    while mehet == "i":
        fordulo += 1
        eredmeny = tipp()
        whowin(eredmeny)
        folytatodik = vege()
        if folytatodik == 0:
            mehet = tovabb()
        else:
            allas(fordulo)


ai = Player("CPU", 0)
human_name = input("Kérem a neved: ")
human = Player(human_name, 0)


main()
print("\nKösz a játékot kedves {}! \nRemélem még találkozunk.".format(human_name))