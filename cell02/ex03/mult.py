print("Enter the firtst number: ")
first_number = int(input())
print("Enter the second number: ")
second_number = int(input())
sum = first_number + second_number
print(sum);
if (sum < 0):
    print("This number is negative.");
elif (sum > 0):
    print("This number is positive");
else:
    print("This number is both positive and negative.");
print("")
