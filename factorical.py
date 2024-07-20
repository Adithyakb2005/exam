a = int(input("Enter a number: "))
f = 1
if a < 0:
    print("does not work")
elif a == 0:
    print("Factorial is 1.")
else:
    for i in range(1, a + 1):
        f *= i
    print(f)
