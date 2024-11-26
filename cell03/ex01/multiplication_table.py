print("Enter a number ")
input = int(input())
for number in range(10):
    sum = input * number
    if input < 0:
        print(number, "*", "(-", abs(input), ") =", sum)
    else:
        print(number, " * ", input, " = ", sum)

