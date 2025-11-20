##crea te a function that calculates any one age based on the current year 202
import datetime

def calculate_age():
    current_year = datetime.datetime.now().year
    birth_year = int(input("Enter your birth year: "))
    age  = current_year - birth_year
    print(age)
    return age
calculate_age()




    
