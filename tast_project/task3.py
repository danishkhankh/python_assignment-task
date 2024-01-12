#####################################################################
# Task 2: Generate Fibonacci Series
#####################################################################


def func(n):
    fb = [0, 1]

    while len(fb) < n:
        next_number = fb[-1] + fb[-2]
        fb.append(next_number)

    return fb

n = int(input("Enter the number : "))

if n < 0:
    print("Please enter a non-negative integer. : ")
else:
    fb = func(n)
    print(f"Fibonacci sequence up to {n} terms: {fb}")



