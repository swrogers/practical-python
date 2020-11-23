# bounce.py
#
# Exercise 1.5

height = 100 # meters
rebound_height = (3 / 5)

for i in range(10):
    height = height * rebound_height
    print(i+1, round(height, 4))

