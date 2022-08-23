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

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Fallido")
