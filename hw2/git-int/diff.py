import re
import sys

#print('Hello, world!')
#'pythonregex.check'
#'pythonregex.txt'
regexinput = open(sys.argv[1], 'r')
inputfile = open(sys.argv[2], 'r')

#print(regexinput.read())
#print(samplefile.read())
passed = True
line_counter = 0

for line1 in regexinput:
    for line2 in inputfile:
        line_counter=line_counter+1

        if re.search(line1, line2):
            #print("SAME\n")
            pass
        else:
        	print("DIFFERENCE on line % 2d :" %(line_counter))
        	#print(line_counter)
        	print(line1)
        	print(line2)
        	passed = False
        break

if(passed == False):
    print("DID NOT PASS TESTCASE, PLEASE SEE LINE DIFFERENCES ABOVE")
else:
	print("Passed!")

regexinput.close()
inputfile.close()