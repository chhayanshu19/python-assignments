import math

print("Angle\tsin\tcos\ttan")

for angle in range(0,91,15):
    rad = math.radians(angle)
    print(f"{angle}\t{math.sin(rad):.2f}\t{math.cos(rad):.2f}\t{math.tan(rad):.2f}")

    