
def day_of_week(day, month, year):
    d = day
    y = year
    m = month
    h = (13 * m + 3) // 5 + d + y + y // 4 - y // 100 + y // 400
    h %= 7

    day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    return day_names[h]

print(day_of_week(23,2,2010))



#def friday(year):
    # List comprehension to find all Fridays that fall on the 13th in the given year
   # return [[13, month] for month in range(1, 13) if day_of_week(13, month, year) == 'Friday']
#
# Example usage
#year = 2024
#print(friday(year))  # Output: [(13, 5), (13, 1)]
