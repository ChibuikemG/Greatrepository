
# Exercise 1: Create a list of 5 of your favorite fruits and print them.
Fruits = []

Fruits = ["Strawberry", "Apple", "Orange", "Pineapple", "Mango"]
print(Fruits)

# Exercise 2: Add a new fruit to the list and print the updated list.
Fruits = ["Strawberry", "Apple", "Orange", "Pineapple", "Mango"]
Fruits.append("Banana")
print(Fruits)

# Exercise 3: Remove the third fruit from the list and print the updated list.
Fruits.pop(2)
print(Fruits)

# Exercise 4: Sort the list in alphabetical order and print it.
Fruits.sort()
print(Fruits)

# Exercise 5: Reverse the order of the list and print it.
Fruits.reverse()
print(Fruits)

# Exercise 6: Print the length of the list.
print(len(Fruits))

# Exercise 7: Check if a certain fruit is in the list and print a corresponding message.
fruit_to_check = "Mango"  # You can change this to any fruit you want to check

if fruit_to_check in Fruits:
    print(f"{fruit_to_check} is in the list.")
else:
    print(f"{fruit_to_check} is not in the list.")

# Exercise 8: Print each fruit in the list using a for loop.
for fruit in Fruits:
    print(fruit)

# Exercise 9: Create a new list that contains the length of each fruit name and print it.
fruit_lengths = [len(fruit) for fruit in Fruits]
print(fruit_lengths)

# Exercise 10: Create a list of numbers from 1 to 10 and print the squares of each number.
Numbers = []
Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in Numbers:
    print(f"The square of {number} is {number ** 2}")

#OR
Numbers = list(range(1, 11))

# Print the squares of each number using a for loop
for number in Numbers:
    print(f"The square of {number} is {number ** 2}")
