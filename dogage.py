dogAge = int(input("DogAge: "))
if (dogAge <= 2 ):
    humAge = dogAge * 12
else:
    extraYears = int(input("number of years of the dog - 2:"))
    #24 for the first 2 years and then 6 X the rest of the years
    startAge = 24
    humAge = startAge + (extraYears * 6)
#end if
print(
