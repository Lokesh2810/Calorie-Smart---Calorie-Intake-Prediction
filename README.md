# Calories Intake Prediction System 
### In this project I have developed a model which predicts calories consumption of a person on daily basis. The predictions are based on follwoing factors 
#### 1. Age 
#### 2. Gender
#### 3. Height
#### 4. Weight
#### 5. BMI
#### 6. BMR
#### 7. Activity Level 
## Dataset :- 
#### For this Project I have used Diet plan recommendation dataset available on [Kaggle](https://www.kaggle.com/datasets/vechoo/diet-plan-recommendation) 
#### This dataset contains parameters such as age,gender,height,weight, BMI, BMR, Calories to Maintain weight, BMI tags and labels with 10.7k entries 
## EDA and Preprocessing:-
#### Preprocessing of Data and EDA on preprocessed data is done in [eda.ipynd](eda.ipynb) file. Here I did univariate analysis to learn about data in depth followed by making a heatmap to find the corelation between various feature 
#### For preprocessing 
#### 1. I used label encoder from sk learn to convert gender data into integers 
#### 2. Converted Activity level data into integer values in range [1,5] for better Understanding
#### 3. Removed High corelated features such as BMI_tags, lable
#### 4. Performed Eda on preprocessed dataset using violin plot, box plot etc. and saved final dataset as preprocessed_data
## Model selection :-
#### In [Models.ipynb](Models.ipynb) I scaled the variables and then appied them on following Models
#### 1. Linear regression
#### 2. Random forest
#### 3. Support Vector Machine
#### 4. Decision trees
#### 5. Neural Networks 
#### Further I performed Hyperparameter Tuning on best of these models based on Mean absolute score and Mean squared score and saved the model in pickle [file](Final_Model.pkl)
## Command Line Application:-
#### In [calorie_intake_prediction.py](calorie_intake_prediction.py) You can find the implementation of the model for real time
## dependencies
#### This [File](dependencies.ipynb) contains all the liberaries used in this project 

