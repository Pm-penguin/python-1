#PRAGYA MISHRA 0801IT221158
def getSum(n): 
    sum = 0
    for digit in str(n):  
      sum += int(digit)       
    return sum
n = int(input("Enter a number: "))
print(getSum(n))