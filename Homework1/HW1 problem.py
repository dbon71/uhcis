#David Bonilla
#CIS2348 Ratner
#PSID:1913106
#Current Code
print('Current Day')
current_month = int(input())
current_day = int(input())
current_year = int(input())
#Birthday code
birth_month = int(input())
birth_day = int(input())
birth_year = int(input())
age = int(current_year - birth_year)
if (birth_month == current_month) and (birth_day == current_day):
    print('Happy Birthday! You are', age, 'years old')
else:
    print('Your are', age, 'years old')



