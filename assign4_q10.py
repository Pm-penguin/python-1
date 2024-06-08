#PRAGYA MISHRA 0801IT221158
def leap_year(year):
    
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
year = int(input("Enter a year: "))
if(leap_year(year)):
    print("LEAP YEAR")
else:
    print("NOT A LEAP YEAR")
    