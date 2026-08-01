#ASSIGNMENT 1

#LEVEL 1

#Q1:- Write a program to input marks in five subjects and calculate the total, percentage, and grade.

m1 = float(input("Enter marks of Subject 1: "))
m2 = float(input("Enter marks of Subject 2: "))
m3 = float(input("Enter marks of Subject 3: "))
m4 = float(input("Enter marks of Subject 4: "))
m5 = float(input("Enter marks of Subject 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

print("Total Marks =", total)
print("Percentage =", percentage)

if percentage >= 90:
    print("Grade = A")
elif percentage >= 80:
    print("Grade = B")
elif percentage >= 70:
    print("Grade = C")
elif percentage >= 60:
    print("Grade = D")
elif percentage >= 40:
    print("Grade = E")
else:
    print("Grade = F")

#Q2:- Write a program to determine whether a given year is a leap year.

'''year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")'''

#Q3:- Write a program to find the largest and second largest among three numbers.

'''a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

numbers = [a, b, c]
numbers.sort()

print("Largest =", numbers[2])
print("Second Largest =", numbers[1])'''

#Q4:-Write a program to calculate an electricity bill based on slab rates.

'''units = int(input("Enter electricity units consumed: "))

bill = 0

if units <= 100:
    bill = units * 5

elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7

else:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10

print("Electricity Bill = ₹", bill)'''

#Q5 :- Write a program to check whether a number is an Armstrong number.

'''num = int(input("Enter a number: "))

temp = num
digits = len(str(num))
sum = 0

while temp > 0:
    digit = temp % 10
    sum = sum + (digit ** digits)
    temp = temp // 10

if sum == num:
    print(num, "is an Armstrong Number")
else:
    print(num, "is not an Armstrong Number")'''

#Q6:- . Input a string and print the first 3 characters, last 3 characters, every alternate character, and the reversed string.

'''string = input("Enter a string: ")

print("First 3 characters:", string[:3])
print("Last 3 characters:", string[-3:])
print("Every alternate character:", string[::2])
print("Reversed string:", string[::-1])'''

#Q7:- Count the number of vowels, consonants, digits, and special characters in a string.

'''string = input("Enter a string: ")

vowels = 0
consonants = 0
digits = 0
special = 0

for ch in string:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif not ch.isspace():
        special += 1

print("Vowels =", vowels)
print("Consonants =", consonants)
print("Digits =", digits)
print("Special Characters =", special)'''

#Q8 :- Check whether a string is a palindrome using slicing

'''string = input("Enter a string: ")

if string == string[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")'''

#Q9:- Find the frequency of each character in a string.

'''string = input("Enter a string: ")

for ch in string:
    if string.count(ch) > 0:
        print(ch, ":", string.count(ch))
        string = string.replace(ch, "")'''

#Q10:-  Remove all spaces from a string and count the number of words.

'''string = input("Enter a sentence: ")

no_spaces = string.replace(" ", "")
word_count = len(string.split())

print("String without spaces:", no_spaces)
print("Number of words:", word_count)'''

#Q11:- Print all prime numbers between 1 and N.

'''n = int(input("Enter the value of N: "))

print("Prime numbers between 1 and", n, "are:")

for num in range(2, n + 1):
    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")'''

#Q12:-  Generate the Fibonacci sequence up to N terms using loops.

'''n = int(input("Enter the number of terms: "))

a = 0
b = 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c'''

#Q13:- Find all factors of a given number.

'''num = int(input("Enter a number: "))

print("Factors of", num, "are:")

for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")'''

#Q14:- Check whether a number is a Perfect Number

'''num = int(input("Enter a number: "))

sum = 0

for i in range(1, num):
    if num % i == 0:
        sum += i

if sum == num:
    print(num, "is a Perfect Number")
else:
    print(num, "is not a Perfect Number")'''

#Q15:- Print Floyd's Triangle up to N rows.

'''rows = int(input("Enter the number of rows: "))

num = 1

for i in range(1, rows + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()'''

#Q16:- Find the largest, smallest, and average value in a list.

'''numbers = list(map(int, input("Enter list elements separated by spaces: ").split()))

largest = max(numbers)
smallest = min(numbers)
average = sum(numbers) / len(numbers)

print("Largest =", largest)
print("Smallest =", smallest)
print("Average =", average)'''

#Q17:-Remove duplicate elements from a list while maintaining the original order.

'''numbers = list(map(int, input("Enter list elements separated by spaces: ").split()))

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("List after removing duplicates:")
print(unique)'''

#Q18:-  Find the second largest and second smallest element in a list.

'''numbers = list(map(int, input("Enter list elements separated by spaces: ").split()))

numbers = list(set(numbers))
numbers.sort()

print("Second Smallest =", numbers[1])
print("Second Largest =", numbers[-2])'''

#Q19:- Separate even and odd numbers from a list into two different lists.

'''numbers = list(map(int, input("Enter list elements separated by spaces: ").split()))

even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even Numbers:", even)
print("Odd Numbers:", odd)'''

#20:- Rotate a list by K positions to the left.

'''numbers = list(map(int, input("Enter list elements separated by spaces: ").split()))

k = int(input("Enter number of positions to rotate: "))

k = k % len(numbers)

rotated = numbers[k:] + numbers[:k]

print("Rotated List:")
print(rotated)'''


#LEVEL 2


#Q1:-  Create a list of squares of numbers from 1 to 50 using list comprehension.

'''squares = [i ** 2 for i in range(1, 51)]

print(squares)'''

#Q2:- Generate a list containing only prime numbers between 1 and 100 using list comprehension.

'''primes = [
    num
    for num in range(2, 101)
    if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))
]

print(primes)'''

#Q3:-Convert a list of strings into uppercase using list comprehension.

'''words = input("Enter words separated by spaces: ").split()

uppercase_words = [word.upper() for word in words]

print(uppercase_words)'''

#Q4:- Create a list containing the lengths of each word in a sentence.

'''sentence = input("Enter a sentence: ")

words = sentence.split()

lengths = [len(word) for word in words]

print(lengths)'''

#Q5:- Remove empty strings and strings containing only spaces from a list using list comprehension.

'''strings = ["Python", "", "Java", "   ", "C++", "HTML", " ", "CSS"]

result = [s for s in strings if s.strip()]

print(result)'''

#Q6:- Write a function to check whether a number is prime.

'''def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


number = int(input("Enter a number: "))

if is_prime(number):
    print(number, "is a Prime Number")
else:
    print(number, "is not a Prime Number")'''

#Q7:- Write a function to calculate the GCD of two numbers.

'''def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("GCD =", gcd(num1, num2))'''

#Q8:-  Write a function that returns the second largest element of a list.

'''def second_largest(lst):
    lst = list(set(lst))
    lst.sort()
    return lst[-2]


numbers = list(map(int, input("Enter list elements: ").split()))

print("Second Largest =", second_largest(numbers))'''

#Q9:- Write a function that accepts a sentence and returns the longest word.

'''def longest_word(sentence):
    words = sentence.split()
    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest


sentence = input("Enter a sentence: ")

print("Longest Word =", longest_word(sentence))'''

#Q10 :- Write a function that merges two lists and removes duplicate elements.

'''def merge_lists(list1, list2):
    merged = list1 + list2
    result = []

    for item in merged:
        if item not in result:
            result.append(item)

    return result


list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

print("Merged List =", merge_lists(list1, list2))'''

#Q11 :-Find the common elements between two lists without using sets.

'''list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

common = []

for item in list1:
    if item in list2 and item not in common:
        common.append(item)

print("Common Elements:", common)'''

#Q12:-Find the missing number from a list containing numbers from 1 to N.

'''numbers = list(map(int, input("Enter the numbers: ").split()))
n = int(input("Enter the value of N: "))
expected_sum = n * (n + 1) // 2
actual_sum = sum(numbers)
missing = expected_sum - actual_sum
print("Missing Number =", missing)'''

#Q13:- Find the frequency of every element in a list.

'''numbers = list(map(int, input("Enter list elements: ").split()))

visited = []

for num in numbers:
    if num not in visited:
        print(num, ":", numbers.count(num))
        visited.append(num)'''

#Q14:- Sort a list in ascending order without using the sort() method.

'''numbers = list(map(int, input("Enter list elements: ").split()))

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

print("Sorted List:")
print(numbers)'''

#Q15:- Print a diamond star pattern

'''rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    print("* " * i)

for i in range(rows - 1, 0, -1):
    print(" " * (rows - i), end="")
    print("* " * i)'''


#Q16:- Write a program to safely divide two numbers using exception handling.

'''try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 / num2

    print("Result =", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Please enter valid numbers.")'''

#Q17:-Accept integer input until a valid integer is entered using try-except.

'''while True:
    try:
        number = int(input("Enter an integer: "))
        print("You entered:", number)
        break

    except ValueError:
        print("Invalid input! Please enter an integer.")'''

#Q18:- Handle IndexError while accessing list elements.

'''numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter index: "))
    print("Element =", numbers[index])

except IndexError:
    print("Error: Index out of range.")

except ValueError:
    print("Error: Please enter a valid integer index.")'''

#Q19:- Handle FileNotFoundError while opening a file.

'''try:
    file = open("data.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("Error: File not found.")'''

#Q20:-  Build a menu-driven calculator that handles invalid inputs and division by zero using try-except.

'''while True:
    print("\n===== Calculator =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 5:
            print("Calculator Closed.")
            break

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            print("Result =", num1 + num2)

        elif choice == 2:
            print("Result =", num1 - num2)

        elif choice == 3:
            print("Result =", num1 * num2)

        elif choice == 4:
            print("Result =", num1 / num2)

        else:
            print("Invalid Choice!")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    except ValueError:
        print("Error: Please enter valid numeric values.")'''


#LEVEL 3

#Q1:-  Find the factorial of a number using recursion.

'''def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


num = int(input("Enter a number: "))

print("Factorial =", factorial(num))'''

#Q2:- Generate the Fibonacci sequence using recursion.

'''def fibonacci(n):
    if n == 0:
        return 0

    elif n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


terms = int(input("Enter the number of terms: "))

print("Fibonacci Series:")

for i in range(terms):
    print(fibonacci(i), end=" ")'''

#Q3:- Find the sum of digits of a number using recursion.

'''def sum_digits(n):
    if n == 0:
        return 0

    return (n % 10) + sum_digits(n // 10)


num = int(input("Enter a number: "))

print("Sum of Digits =", sum_digits(num))'''

#Q4:- Reverse a string using recursion

'''def reverse_string(text):
    if len(text) == 0:
        return ""

    return reverse_string(text[1:]) + text[0]


string = input("Enter a string: ")

print("Reversed String =", reverse_string(string))'''

#Q5:- Solve the Tower of Hanoi problem using recursion.

'''def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return

    tower_of_hanoi(n - 1, source, destination, auxiliary)

    print("Move disk", n, "from", source, "to", destination)

    tower_of_hanoi(n - 1, auxiliary, source, destination)


disks = int(input("Enter the number of disks: "))

tower_of_hanoi(disks, "A", "B", "C")'''

#Q6:- Write a recursive function to determine whether a string is a palindrome.

'''def palindrome(text):
    if len(text) <= 1:
        return True

    if text[0] != text[-1]:
        return False

    return palindrome(text[1:-1])


string = input("Enter a string: ")

if palindrome(string):
    print("Palindrome")
else:
    print("Not a Palindrome")'''

#Q7:- Use list comprehension and a helper function to create a list containing only prime numbers.

'''def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True
primes = [num for num in range(1, 101) if is_prime(num)]
print(primes)'''

#Q8:- Read numbers until 'stop' is entered, handle invalid inputs using try-except, then calculate minimum, maximum, average, and median.

'''numbers = []

while True:
    value = input("Enter a number (or 'stop' to finish): ")

    if value.lower() == "stop":
        break

    try:
        numbers.append(float(value))
    except ValueError:
        print("Invalid input! Please enter a valid number.")

if len(numbers) == 0:
    print("No numbers entered.")
else:
    numbers.sort()
    minimum = numbers[0]
    maximum = numbers[-1]
    average = sum(numbers) / len(numbers)
    n = len(numbers)
    if n % 2 == 0:
        median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2
    else:
        median = numbers[n // 2]

    print("Minimum =", minimum)
    print("Maximum =", maximum)
    print("Average =", average)
    print("Median =", median)'''

#Q9:- Write a recursive function to flatten a nested list.

'''def flatten(lst):
    result = []

    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)

    return result

nested_list = [1, [2, [3, 4], 5], [6, 7], 8]

print("Original List:")
print(nested_list)

print("Flattened List:")
print(flatten(nested_list))'''

#Q10:- Create a Student Record Management System using functions, lists, loops, list comprehensions, exception handling, and file handling.

'''def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))

    file = open("students.txt", "a")
    file.write(f"{roll},{name},{marks}\n")
    file.close()

    print("Student record added successfully.")


def display_students():
    try:
        file = open("students.txt", "r")

        print("\nStudent Records:")
        print("----------------------------")

        for line in file:
            roll, name, marks = line.strip().split(",")
            print("Roll:", roll)
            print("Name:", name)
            print("Marks:", marks)
            print("----------------------------")

        file.close()

    except FileNotFoundError:
        print("No student records found.")


while True:
    print("\n===== Student Record Management =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_student()

        elif choice == 2:
            display_students()

        elif choice == 3:
            print("Program Closed.")
            break

        else:
            print("Invalid Choice!")

    except ValueError:
        print("Please enter a valid integer.")'''

