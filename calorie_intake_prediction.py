# This is the final part of this project where we are building a command line application to predict the calories of a person

# Importing necessary files
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler

# Loading trained Model
model = joblib.load("Final_Model.pkl")

while True:
    age = int(input("Enter your age (or enter -1 to exit): "))
    if age == -1:
        break
    # Taking user Input
    gender = input("Enter your gender (male/female): ")
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    activity_level = float(
        input(
            "Enter your activity level (1 for sedentary, 2 for light activity, 3 for moderate activity, 4 for active, 5 for very active): "
        )
    )

    # Preprocessing The user DATA

    # Encoding gender
    if gender.lower() == "male":
        encoded_gender = 1
    else:
        encoded_gender = 0

    # BMI Calculation
    BMI = weight / height**2

    # BMR Calculation
    if encoded_gender == 1:
        BMR = 66.5 + (13.75 * weight) + (5 * height) - (6.755 * age)
    else:
        BMR = 655.1 + (9.6 * weight) + (1.8 * height) - (4.7 * age)

    # Performing feature scaling
    user_input = np.array(
        [[age, weight, height, encoded_gender, BMI, BMR, activity_level]]
    )

    scaler = StandardScaler()

    # Scaling the user Input
    scaled_input = scaler.fit_transform(user_input)

    # Making Prediction
    calorie_intake_prediction = model.predict(scaled_input)

    print("Your predicted calorie intake is:", calorie_intake_prediction)
    print("Application exited.")
