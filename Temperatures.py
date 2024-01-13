import sys
import math

closest_temp_to_zero = 10000 #max margin


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

    if abs(t) < abs(closest_temp_to_zero):
        closest_temp_to_zero = t

    if abs(t) == abs(closest_temp_to_zero) and t > closest_temp_to_zero:
        closest_temp_to_zero = t

if closest_temp_to_zero == 10000: 
     closest_temp_to_zero = 0

print(closest_temp_to_zero)
