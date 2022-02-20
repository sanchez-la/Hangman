# Write your code here

# imports
import random


def main():
    while True:
        try:
            print("H A N G M A N\n")
            msg = input("Type 'play' to play the game, 'exit' to quit: ")
            if msg == "play":
                break
            elif msg == "exit":
                continue
        except EOFError:
            exit()
    print("H A N G M A N\n")
    lst = ['python', 'java', 'kotlin', 'javascript']
    wrd = random.choice(lst)
    charl = ["-" for i in wrd]
    x = "".join(charl)
    wrdi = set(wrd)
    count = 0
    lusadas = set()
    global item
    while True:
        try:
            if count >= 8:
                print("You lost!")
                break
            print()
            print(x)
            item = input("Input a letter: ")
            if len(item) != 1:
                print("You should input a single letter")
                continue
            if not item.islower():
                print("Please enter a lowercase English letter")
                continue
            if item in charl or item in lusadas:
                print("You've already guessed this letter")
                continue
            wrdi.remove(item)
            for i in range(len(wrd)):
                if item == wrd[i]:
                    charl[i] = item
                    x = "".join(charl)
            if x.isalpha():
                print()
                print(x)
                print("You guessed the word!\nYou survived!")
                break
        except KeyError:
            count += 1
            lusadas.add(item)
            print("That letter doesn't appear in the word")
    # print("Thanks for playing!")
    # print("We'll see how well you did in the next page")


if __name__ == "__main__":
    main()
