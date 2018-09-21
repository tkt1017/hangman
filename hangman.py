# modified #1

import random

def hangman(word):
    wrong = 0
    stages = [
        "",
        "___________",
        "|          ",
        "|      |   ",
        "|      o   ",
        "|     /|\  ",
        "|     / \  ",
    ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    inplist = []
    print("ハングマンへようこそ！")
    print("word は {} です.".format(" ".join(board)))
    while wrong < len(stages) - 1:
        print("\n")
        msg ="1文字を予想してね."
        char = input(msg)
        if len(char) == 1:
            if char not in inplist:
                inplist.append(char)
                if char in rletters:
                    bcind = -1
                    crletters = rletters
                    while True:
                        try:
                            cind = crletters.index(char)
                            #print("dbg : cind is {}.".format(cind)) #dbg
                            bcind += cind + 1
                            #print("dbg : bcind is {}.".format(bcind)) #dbg
                            board[bcind] = char
                            rletters[bcind] = '$'
                            x = "".join(rletters[bcind+1:len(crletters)])
                            #print("dbg : x is {}.".format(x)) #dbg
                            crletters = list(x)
                        except:
                            break
                else:
                    wrong += 1
                print(" ".join(board))
                e = wrong + 1
                print("\n".join(stages[0:e]))
                if "_" not in board:
                    print("あなたの勝ち！")
                    print(" ".join(board))
                    win = True
                    break
            else:
                print("Error : 以前入力した文字です.")
        else:
             print("Error : 2文字以上です.")
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は {}.".format(word))

words = ["cat","dog","sheep","elephant"]
num = random.randint(0,len(words)-1)

hangman("sheep") 