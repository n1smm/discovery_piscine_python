print("Enter a number les than 25")
input = int(input())
if input > 25:
    print("Error")
    exit(1)
while input <= 25:
    print("Inside the loop, my variable is " + str(input))
    input += 1

