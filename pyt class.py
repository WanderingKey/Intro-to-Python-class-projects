height = float(input("Enter your height in cm"))
weight = float(input("Enter your weight in kg"))

BMI = weight / (height/100)**2
print(f"your BMI is {BMI}")
if BMI <= 18.5:
    print("you are underweight")
elif BMI <= 24.9:
    print("you are healthy")
elif BMI <= 29.9:
    print("You are overweight")
else:
    print("you are obese")