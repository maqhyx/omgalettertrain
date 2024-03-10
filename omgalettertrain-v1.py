import os
import sys

def omgalettertrain(sentence):
    wordslist = sentence.split(" ")
    wordslist.pop()


    l1 = ("       #######")
    l2 = ("       ####")
    l3 = ("      ###")
    l4 = ("     ##")           
    l5 = ("    #   _________ ") 
    l6 = ("   _][__|[] []  | ")
    l7 = ("  (_____|_______|-")
    l8 = (" /O--O O--O O--O  ")
    l9 = ("==================")



    for l in range(len(wordslist)):
        l5 += "_" * (len(wordslist[l])+4) + " "
        l6 += "| " + wordslist[l] + " | "
        l7 += "|" + "_"*(len(wordslist[l])+2) + "|-"
        l8 += "O" + " "*(len(wordslist[l])+2) + "O" + " "
        l9 += "=" * (len(wordslist[l])+5)

    print(l1)
    print(l2)
    print(l3)
    print(l4)
    print(l5)
    print(l6)
    print(l7)
    print(l8)
    print(l9)

    

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "!help":
            print("""
  omgalettertrain : help
              omgalettertrain <string>              | command (argumant should be string, typing "!help" displays this)
              
""")
            
        elif sys.argv[1] == "!info":
            print("""
  omgalettertrain : info
              created by maqhyx, MIT license, github.com/maqhyx/omgalettertrain
              
""")
        else:
            var = ""
            for i in range(1, len(sys.argv)):
                if i == len(sys.argv):
                    var = var + sys.argv[i]
                else:
                    var = var + sys.argv[i] + " "
            omgalettertrain(var)
    else:
        print("WARNING : No arguments")









