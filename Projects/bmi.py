def Calculate_bmi():
    print("BMI Calculator")

    
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    
    bmi = weight / (height ** 2)

    print(f"Your BMI is: {bmi:.2f}")

    if bmi < 18.5:
        print("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        print("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        print("You are overweight.")
    elif 30 <= bmi < 39.9:
        print("You are obese.")
    else:
        print("You are severly obese.")

Calculate_bmi()