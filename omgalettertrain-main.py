import sys
import os
import warnings
import random

NOCOLOR = "\033[0m"

COLORS_SI = ["\u001b[32m", "\u001b[33m", "\u001b[35m", "\u001b[36m", "\u001b[32;1m", "\u001b[33;1m",
             "\u001b[34;1m", "\u001b[35;1m", "\u001b[36;1m", "\x1b[1;31m"]
SYMBOLS = ["Warning : "]
modes = ["cful", "cless", "help"]
os.system("")

warnings.simplefilter("ignore")
def omgalettertrain(mode, sentence):
    if mode not in modes:
        print("""
              +++++++++++++++++++++++++++++++++++++++++++++++
              Unable to make a train because of unknown mode.
              +++++++++++++++++++++++++++++++++++++++++++++++
              """)
        return None
    elif mode == "help":
        print("""
              OMGACOLORTRAIN : 
              omgacolortrain                              | command (would give an error because of no args)
              omgacolortrain <mode> <string>              | full command as it should be written 
                              ^        ^
                              |        |
                              |        any your string
                              |
                            mode -> can only be:
                                            cful - for colored train
                                            cless - for console default color train
                                            help - displays this                                           

        """)
        return None

    else:
        wordslist = sentence.split(" ")
        if mode == "cful":
            colortrain = COLORS_SI[random.randrange(0, len(COLORS_SI))]
        else:
            colortrain = ""

    l1 = (colortrain + "       #######")
    l2 = (colortrain + "       ####")
    l3 = (colortrain + "      ###")
    l4 = (colortrain + "     ##")           
    l5 = (colortrain + "    #   _________ ") 
    l6 = (colortrain + "   _][__|[] []  | ")
    l7 = (colortrain + "  (_____|_______|-")
    l8 = (colortrain + " /O--O O--O O--O  ")
    l9 = (colortrain + "==================")
    
    
    
    for l in range(len(wordslist)):
        if mode == "cful":
            colortrain = COLORS_SI[random.randrange(0, len(COLORS_SI))]
        else:
            colortrain = ""
        l5 +=  colortrain + "_" * (len(wordslist[l])+4) + " "
        l6 += colortrain + "| " + wordslist[l] + " | "
        l7 += colortrain + "|" + "_"*(len(wordslist[l])+2) + "|-"
        l8 += colortrain + "O" + " "*(len(wordslist[l])+2) + "O" + " "
        l9 += colortrain + "=" * (len(wordslist[l])+5)
    
    print(l1)
    print(l2)
    print(l3)
    print(l4)
    print(l5)   
    print(l6)
    print(l7)
    print(l8)
    print(l9)
    if mode == "cful":
        print(NOCOLOR)
    else:
        pass


if __name__ == "__main__":
    if len(sys.argv) > 2:
        omgalettertrain(sys.argv[1], sys.argv[2])

    
    
    


            





