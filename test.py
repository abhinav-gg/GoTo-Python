from goto_plus import *
gotoconfig(__file__)
j = 1
i = 1
print(str(i*j).rjust(4), end="") # comment this line when done
i += 1
if i < 13:
    #print("GOING TOO\n\n\n\n")
    goto(5)
print("\n") # comment this line when done
j += 1
if j < 13:
    goto(4)
####################
###KEY TIPS###
#1) Use if statements and do not use goto in for or while loops
#2) Do not alter the goto command or try to goto any line number in the goto function
#3) Remember that editing code affects the line numbers of all the lines beneath and so every goto statement will need to be updated
#################### ENJOY

#pypi-AgENdGVzdC5weXBpLm9yZwIkNzc5NWFjOGItNGEyYy00YmZmLTkxMDktNTQyMjE4YWZkMjViAAIRWzEsWyJnb3RvLWxpbmUiXV0AAixbMixbImYyZGU0MDU5LTU0OWItNGNlOS1iNzk3LTY0ZjUyNDhkMTBlOCJdXQAABiD1lRPJw3nkpfNvszHIurBv9lNQeHszwryw6fhBhpvV7w
 
