from datetime import date 

d1 = date(2025, 9, 18)
d2 = date(2025, 9, 20)

diff = d2 - d1
print("Number of days between two dates: ",diff.days)