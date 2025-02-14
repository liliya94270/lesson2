def is_year_leap(year):
    return year % 4 == 0

year = int(input("Type a year: "))
print(f"Год {year}: {is_year_leap(year)}")
