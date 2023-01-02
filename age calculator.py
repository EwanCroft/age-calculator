import datetime
import os

def calculate_age(day, month, year):
    today = datetime.date.today()
    dob = datetime.date(year, month, day)
    age = today - dob
    years = age.days // 365
    months = (age.days % 365) // 30
    days = (age.days % 365) % 30
    return years, months, days

user = os.getlogin()
user_dob = input("Enter your date of birth in any format: ")
try:
    dob = datetime.datetime.strptime(user_dob, "%d/%m/%Y")
except ValueError:
    try:
        dob = datetime.datetime.strptime(user_dob, "%m/%d/%Y")
    except ValueError:
        dob = datetime.datetime.strptime(user_dob, "%Y/%m/%d")
day, month, year = dob.day, dob.month, dob.year
your_age = calculate_age(day, month, year)

if your_age[0] == 1:
    print(f"{user}, you are {your_age[0]} year, {your_age[1]} months, and {your_age[2]} days old.")
else:
    print(f"{user}, you are {your_age[0]} years, {your_age[1]} months, and {your_age[2]} days old.")