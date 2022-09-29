###PLACE ME AT THE TOP OF YOUR CODE### (this function can not be imported as it requires the __file__ var of the specific file it is used in)
def goto(line):
    with open(__import__("os").path.abspath(__file__), "r") as f: content = [i.replace("    ", "\t") for i in f.readlines()]
    try: exec("".join(content[(line-1):]), globals())
    except SystemExit: raise __import__("sys").exit()       
    except RecursionError: raise __import__("sys").exit("GoTo Exception - GoTo has formed a loop.")
    except IndentationError:
        while any([i.isalpha() for i in content[(line-1)]]) == False: line += 1
        editout = content[(line-1):]
        for j, i in enumerate(list(content[(line-1):][0].replace(content[(line-1):][0].lstrip(), ""))):
            editout.insert(0, "{}if True:\n".format('\t' * (len(list(content[(line-1):][0].replace(content[(line-1):][0].lstrip(), "")))-j-1)))
        exec("".join(editout))
    raise __import__("sys").exit()
######################################w
###EXAMPLE OF USE###
j = 1
i = 1
print(str(i*j).rjust(4), end="") # comment this line when done
i += 1
if i < 13:
    goto(18)
print("\n") # comment this line when done
j += 1
if j < 13:
    goto(17)
####################
###KEY TIPS###
#1) Use if statements and do not use goto in for or while loops
#2) Do not alter the goto command or try to goto any line number in the goto function
#3) Remember that editing code affects the line numbers of all the lines beneath and so every goto statement will need to be updated
#################### ENJOY!!!