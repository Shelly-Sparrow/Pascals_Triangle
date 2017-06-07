import math
import sys

from time import clock
import time
import os
text = 'Rows generated:'
filenamestart = 'Pascals Triangle with'
filenameend = 'rows.txt'
endmessage1 = 'Results have been saved under'
endmessage2 = 'in this directoy.'
quotemark = '"'
restart = 0

print("==================================================================")
print("Pascals Triangle Generator - Michael Edwards")
print("==================================================================")
print("Credit to:")
print("Aaron Hall (generator) http://stackoverflow.com/a/24093733")
print("==================================================================")
print("Calculating large numbers of rows will take considerable time,")
print("which will also be affected by your hardware capabilities.")
print("")
print("")

class Tee(object):
    def __init__(self, *files):
        self.files = files
    def write(self, obj):
        for f in self.files:
            f.write(obj)
            f.flush() # If you want the output to be visible immediately
    def flush(self) :
        for f in self.files:
            f.flush()

usernumber = input("Rows needed: ")
print("Working...")

f = open('%s %d %s' % (filenamestart, usernumber, filenameend), 'w')
original = sys.stdout
sys.stdout = Tee(sys.stdout, f)


start_time = time.time() 


# pascals_tri_formula = [] # don't collect in a global variable.
start = clock()

def combination(n, r): # correct calculation of combinations, n choose k
    return int((math.factorial(n)) / ((math.factorial(r)) * math.factorial(n - r)))

def for_test(x, y): # don't see where this is being used...
    for y in range(x):
        return combination(x, y)

def pascals_triangle(rows):
    result = [] # need something to collect our results in
    # count = 0 # avoidable! better to use a for loop, 
    # while count <= rows: # can avoid initializing and incrementing 
    for count in range(rows): # start at 0, up to but not including rows number.
        # this is really where you went wrong:
        row = [] # need a row element to collect the row in
        for element in range(count + 1): 
            # putting this in a list doesn't do anything.
            # [pascals_tri_formula.append(combination(count, element))]
            row.append(combination(count, element))
        result.append(row)
        # count += 1 # avoidable
    return result
# now we can print a result:
for row in pascals_triangle(usernumber+1):
	print(row)
print("===================================================================================")
print '%s %d' % (text, usernumber)
print("Time taken: %s seconds " % (time.time() - start_time))
print '%s %s %s %d %s %s %s' % (endmessage1, quotemark, filenamestart, usernumber, filenameend, quotemark, endmessage2)
print("===================================================================================")

response = raw_input("Type anything to quit or R to restart")
if response in ['r', 'R']:
	print("test")
else:
	print("quit")
	