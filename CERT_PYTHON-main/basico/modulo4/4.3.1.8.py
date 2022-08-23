#Sergio Abisay Cervantes Sánchez 
#20/junio/22

def is_year_leap(year):

    if year<1582:
        print("No dentro del período del calendario Gregoriano")
    elif not(year % 4 ==0):
        return False
    elif not(year % 100==0):
        return True
    elif not(year%400==0):
        return False
    else:
        return True
        

def days_in_month(year, month):
    montDays=[31,28,31,30,31,30,31,30,28,29,30,31,28]
    if is_year_leap(year):
        if month ==2:
            return 29
    return montDays[month -1]


def day_of_year(year, month, day):

    if year <1582:
        return None
    if month > 12 or month < 1:
        return None
    if day > 31 or day <1:
        return None

    totalDays = day
    month = month -1
    while month > 0:
        totalDays += days_in_month(year, month)
        month -=1 
    
    return totalDays

print(day_of_year(2000, 12, 31))