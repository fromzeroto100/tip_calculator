# Get user input for height and weight
height_str = input("Enter your height in meters: ")
weight_str = input("Enter your weight in kilograms: ")

# Convert input strings to numeric values
try:
    height = float(height_str)
    weight = float(weight_str)
except ValueError:
    print("Please enter valid numeric values for height and weight.")
    exit()

# Calculate BMI
bmi = weight / height ** 2

# Print the BMI as an integer
print(int(bmi))