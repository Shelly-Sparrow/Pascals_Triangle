import math
import sys
import atexit
from time import clock
import time
import os

print("==================================================================")
print("Pascals Triangle Generator - Michael Edwards")
print("==================================================================")
print("Credit to:")
print("Aaron Hall (generator) http://stackoverflow.com/a/24093733")
print("Paul McGuire (execution timer) http://stackoverflow.com/a/1557906")
print("==================================================================")
print("Calculating large numbers of rows will take considerable time,")
print("depending on your hardware capabilities.")
print("")
print("")
def secondsToStr(t):
    return "%d:%02d:%02d.%03d" % \
        reduce(lambda ll,b : divmod(ll[0],b) + ll[1:],
            [(t*1000,),1000,60,60])

line = "="*40
def log(s, elapsed=None):
    print line
    print secondsToStr(clock()), '-', s
    if elapsed:
        print "Elapsed time:", elapsed
    print line
    print

def endlog():
    end = clock()
    elapsed = end-start
    log("End Program", secondsToStr(elapsed))

def now():
    return secondsToStr(clock())



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

f = open('ouput.txt', 'w')
original = sys.stdout
sys.stdout = Tee(sys.stdout, f)

usernumber = input("Rows needed: ")
print("Working...") 


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
atexit.register(endlog)
# now we can print a result:
for row in pascals_triangle(usernumber):
	print(row)
