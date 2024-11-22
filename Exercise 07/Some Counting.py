# One number at a time, counting up from 0 to 50
print("Ascending from 0 to 50:")
for i in range(0, 51, 1):
    print(i)

# One number at a time, counting down from 50 to 0
print("\nDescending from 50 to 0:")
for i in range(50, -1, -1):
    print(i)

# One number at a time, counting up from 30 to 50
print("\nAscending from 30 to 50:")
for i in range(30, 51, 1):
    print(i)

# Skipping all other numbers, counting down from 50 to 10
print("\nIgnoring all other numbers, descending from 50 to 10:")
for i in range(50, 9, -2):
    print(i)

# Increasing by five each time from 100 to 200
print("\nCounting up from 100 to 200, adding 5 each time:")
for i in range(100, 201, 5):
    print(i)
