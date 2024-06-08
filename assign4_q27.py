#PRAGYA MISHRA 0801IT221158
print("Numbers divisible by 7 and multiple of 5:")
List=[]
for i in range(1500,2701):
    if i%7==0 and i%5==0:
      List.append(i)
print(List)
