#Exercise 1

num = int(int(input("Enter a number: ")))
if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")

#Exercise 2

score = float(input("Enter your score: "))

if score >= 75:
    grade = 'A'
elif score >= 65:
    grade = 'B'
elif score >= 55:
    grade = 'C'
elif score >= 45:
    grade = 'S'
elif score >= 0:
    grade = 'F'
else:
    grade = 'Invalid score'

print(f"Your grade is: {grade}")
