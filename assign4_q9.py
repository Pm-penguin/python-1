#PRAGYA MISHRA 0801IT221158
import math
def log2(x):
    return math.log10(x) / math.log10(2)
def check(x):
    if log2(x) % 1 == 0:
        print("Yes, the number is a power of 2")
    else:
        print("No, the number is not a power of 2")
num = int(input("Enter a number: "))
check(num)