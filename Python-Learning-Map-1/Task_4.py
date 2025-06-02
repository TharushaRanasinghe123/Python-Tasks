#Exercise 1

n = int(input("Enter how many Fibonacci numbers to generate: "))

a, b = 0, 1
count = 0

if n <= 0 :
    print("Please enter a positive integer")
elif n == 1:
    print(f"Fibonacci sequence up to {n}: {a}")
else:
    print("Fibonacci sequence:")
    while count < n:
        print(a, end=' ')
        next_num = a + b
        a = b
        b = next_num
        count += 1

#Exercise 2

numbers = [10, 20, 30, 40, 50]
total = 0

for num in numbers:
    total += num

print(f"\nThe sum of numbers is: {total}")