def is_year_leap(year):
    if year%100==0:
        if year%400==0:
            return True
        else:
            return False
    elif year%4==0:
            return True
    else:
        return False
   
def days_in_month(year, month):
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
   
    if is_year_leap(year)and month==2:
        return 29
    else:
        return days[month-1]

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
yr = test_years[i]
mo = test_months[i]
print(yr, mo, "->", end="")
result = days_in_month(yr, mo)
if result == test_results[i]:
print("OK")
else:
print("Failed")


def day_of_year(year, month, day):
#
# Write your new code here.
#
    if month == 1:
        return day
    elif month<=12:
        for i in range(1,month):
            day += days_in_month(year,i)
        return day
           

print(day_of_year(2024, 9, 25))
print(day_of_year(2023, 2, 28))
print(day_of_year(2024, 5, 25))
