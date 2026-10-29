#1.
fruits = ["Apple", "Mango", "Banana", "Orange", "Grapes"]

print("Fruits:", fruits)
#2.
numbers = [10, 20, 30, 40, 50]

print("First element:", numbers[0])
print("Last element:", numbers[-1])
print("Third element:", numbers[2])

#3.
colors = ["Red", "Blue", "Green", "Yellow"]

colors[2] = "Pink"

print("Updated colors:", colors)

#4.
numbers = [20, 30, 40]

numbers.append(50)
numbers.insert(0, 10)
numbers.insert(2, 15)

print("Updated list:", numbers)

#5.
students = ["Amit", "Neha", "Rahul", "Priya", "Rohan"]

students.pop(0)
students.pop()
students.remove("Rahul")

print("Remaining students:", students)

#6.
numbers = [25, 10, 45, 5, 30]

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print("Largest number:", largest)
print("Smallest number:", smallest)

#7.
numbers = []

for i in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)

total = sum(numbers)
average = total / 10

print("Sum:", total)
print("Average:", average)

#8.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("Even numbers:", even)
print("Odd numbers:", odd)

#9.

cities = ["Pune", "Mumbai", "Kolhapur", "Nashik"]

city = input("Enter a city name: ")

if city in cities:
    print("City found")
else:
    print("City not found")

#10.
numbers = [10, 20, 30, 40, 50]
reversed_list = []

for num in numbers:
    reversed_list.insert(0, num)

print("Reversed list:", reversed_list)

#11.
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print("First 5:", numbers[:5])
print("Last 5:", numbers[5:])
print("Middle 4:", numbers[3:7])
print("Alternate elements:", numbers[::2])
print("Reverse list:", numbers[::-1])

#12.
numbers = [10, 20, 30, 40, 50, 60]

for i in range(len(numbers)):
    if i % 2 == 0:
        print(numbers[i])

#13.
numbers = [45, 12, 78, 23, 9, 56, 34, 90, 11, 67]

numbers.sort()
print("Ascending order:", numbers)

numbers.sort(reverse=True)
print("Descending order:", numbers)

#14.
numbers = [10, 20, 10, 30, 20, 40, 50]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("Unique elements:", unique)

#15.
numbers = [10, 40, 20, 50, 30]

numbers.sort()

print("Second largest:", numbers[-2])

#16.
students = [
    ["Amit", 101, 85],
    ["Neha", 102, 90],
    ["Rahul", 103, 78]
]

for student in students:
    print("Name:", student[0])
    print("Roll Number:", student[1])
    print("Marks:", student[2])
    print()

#17.
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

result = []

for i in range(3):
    row = []
    for j in range(3):
        row.append(A[i][j] + B[i][j])
    result.append(row)

print("Addition of matrices:")

for row in result:
    print(row)

#18.
cart = []

while True:
    print("\n1. Add item")
    print("2. Remove item")
    print("3. Search item")
    print("4. Display cart")
    print("5. Count items")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item: ")
        cart.append(item)

    elif choice == "2":
        item = input("Enter item to remove: ")
        if item in cart:
            cart.remove(item)
        else:
            print("Item not found")

    elif choice == "3":
        item = input("Enter item to search: ")
        if item in cart:
            print("Item found")
        else:
            print("Item not found")

    elif choice == "4":
        print("Shopping cart:", cart)

    elif choice == "5":
        print("Total items:", len(cart))

    elif choice == "6":
        break

    else:
        print("Invalid choice")

#19.
students = ["Amit", "Neha", "Rahul", "Priya"]

print("Total students:", len(students))

name = input("Enter student name to search: ")

if name in students:
    print("Student is present")
else:
    print("Student is absent")

new_student = input("Enter new student name: ")
students.append(new_student)

absent_student = input("Enter absent student name to remove: ")

if absent_student in students:
    students.remove(absent_student)
else:
    print("Student not found")

print("Updated attendance list:", students)

#20.
books = ["Python", "Java", "C Programming"]

books.append(input("Enter a new book: "))

search_book = input("Enter book to search: ")

if search_book in books:
    print("Book found")
else:
    print("Book not found")

remove_book = input("Enter book to remove: ")

if remove_book in books:
    books.remove(remove_book)
else:
    print("Book not found")

print("All books:", books)
print("Total books:", len(books))

#21.
list1 = [10, 20, 30]
list2 = [40, 50, 60]

list3 = list1 + list2

print("Merged list:", list3)

#22.
list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]

common = []

for num in list1:
    if num in list2:
        common.append(num)

print("Common elements:", common)

#23.
numbers = [10, 20, 10, 30, 20, 10]

for num in numbers:
    if num not in []:
        count = numbers.count(num)
        print(num, "appears", count, "times")

#24.
numbers = [10, 20, 30, 40, 50]

left = numbers[1:] + numbers[:1]
right = numbers[-1:] + numbers[:-1]

print("Left rotation:", left)
print("Right rotation:", right)

#25.
numbers = [10, 20, 10, 30, 20, 40, 30]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("List without duplicates:", unique)

#26.
marks = [
    70, 80, 65, 90, 55,
    75, 85, 60, 95, 50,
    72, 88, 68, 92, 78,
    82, 64, 86, 74, 96
]

highest = marks[0]
lowest = marks[0]
total = 0

for mark in marks:
    if mark > highest:
        highest = mark

    if mark < lowest:
        lowest = mark

    total = total + mark

average = total / len(marks)

above = 0
below = 0

for mark in marks:
    if mark > average:
        above = above + 1
    elif mark < average:
        below = below + 1

print("Highest marks:", highest)
print("Lowest marks:", lowest)
print("Average marks:", average)
print("Students above average:", above)
print("Students below average:", below)

#27.
salaries = [25000, 35000, 55000, 60000, 28000, 75000, 45000]

highest = salaries[0]
lowest = salaries[0]
total = 0
above_50000 = 0
below_30000 = 0

for salary in salaries:
    if salary > highest:
        highest = salary

    if salary < lowest:
        lowest = salary

    total = total + salary

    if salary > 50000:
        above_50000 = above_50000 + 1

    if salary < 30000:
        below_30000 = below_30000 + 1

average = total / len(salaries)

print("Highest salary:", highest)
print("Lowest salary:", lowest)
print("Average salary:", average)
print("Employees earning above 50000:", above_50000)
print("Employees earning below 30000:", below_30000)

#28.
scores = [45, 100, 67, 120, 35, 55, 80, 10, 99, 150]

highest = scores[0]
lowest = scores[0]
total = 0
centuries = 0
half_centuries = 0

for score in scores:
    if score > highest:
        highest = score

    if score < lowest:
        lowest = score

    total = total + score

    if score >= 100:
        centuries = centuries + 1

    elif score >= 50:
        half_centuries = half_centuries + 1

average = total / len(scores)

print("Highest score:", highest)
print("Lowest score:", lowest)
print("Total runs:", total)
print("Average runs:", average)
print("Centuries:", centuries)
print("Half-centuries:", half_centuries)

#29.
temperatures = [
    30, 32, 29, 35, 31, 33, 28, 34, 36, 30,
    31, 37, 32, 29, 35, 33, 38, 30, 34, 31,
    36, 32, 29, 35, 33, 37, 31, 34, 30, 36
]

hottest = temperatures[0]
coldest = temperatures[0]
total = 0

for temp in temperatures:
    if temp > hottest:
        hottest = temp

    if temp < coldest:
        coldest = temp

    total = total + temp

average = total / len(temperatures)

above = 0
below = 0

for temp in temperatures:
    if temp > average:
        above = above + 1
    elif temp < average:
        below = below + 1

print("Hottest temperature:", hottest)
print("Coldest temperature:", coldest)
print("Average temperature:", average)
print("Days above average:", above)
print("Days below average:", below)

#30.
names = ["Amit", "Neha", "Rahul"]
ages = [25, 30, 40]

# Add a patient
name = input("Enter patient name: ")
age = int(input("Enter patient age: "))

names.append(name)
ages.append(age)

# Search for a patient
search_name = input("Enter patient name to search: ")

if search_name in names:
    index = names.index(search_name)
    print("Patient found")
    print("Age:", ages[index])
else:
    print("Patient not found")

# Delete a patient
delete_name = input("Enter patient name to delete: ")

if delete_name in names:
    index = names.index(delete_name)
    names.pop(index)
    ages.pop(index)
    print("Patient deleted")
else:
    print("Patient not found")

# Display all patients
print("\nPatient Details:")

for i in range(len(names)):
    print("Name:", names[i], "Age:", ages[i])

print("Total patients:", len(names))     


