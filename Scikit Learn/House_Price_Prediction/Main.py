import pandas as pd
import numpy as np

# ---------------------------------------------------
# Machine Learning Algorithms
# ---------------------------------------------------

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import AdaBoostRegressor

# ---------------------------------------------------
# Train Test Split
# ---------------------------------------------------

from sklearn.model_selection import train_test_split

# ---------------------------------------------------
# Evaluation Metrics
# ---------------------------------------------------

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# ---------------------------------------------------
# Load Dataset
# ---------------------------------------------------

dataset = pd.read_csv("/Users/namratha/Desktop/python tasks/Scikit Learn/House_Price_Prediction/kc_house_data (1).csv")

# Display First 5 Rows
print("\nFirst 5 Rows of Dataset")
print(dataset.head())

# ---------------------------------------------------
# Input and Output Columns
# ---------------------------------------------------

X = dataset[[
    'bedrooms',
    'bathrooms',
    'sqft_living',
    'sqft_lot',
    'floors',
    'condition',
    'grade',
    'sqft_basement',
    'yr_built',
    'yr_renovated'
]]

y = dataset['price']

# ---------------------------------------------------
# Split Dataset into Training and Testing
# ---------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ---------------------------------------------------
# Create Models
# ---------------------------------------------------

models = {

    "1. Linear Regression":
        LinearRegression(),

    "2. Decision Tree Regressor":
        DecisionTreeRegressor(random_state=42),

    "3. Random Forest Regressor":
        RandomForestRegressor(
            n_estimators=100,
            random_state=42
        ),

    "4. KNN Regressor":
        KNeighborsRegressor(
            n_neighbors=5
        ),

    "5. Support Vector Regressor":
        SVR(),

    "6. Gradient Boosting Regressor":
        GradientBoostingRegressor(
            random_state=42
        ),

    "7. AdaBoost Regressor":
        AdaBoostRegressor(
            random_state=42
        )
}

# ---------------------------------------------------
# Train and Evaluate All Models
# ---------------------------------------------------

for name, model in models.items():

    print("\n====================================")
    print("Algorithm :", name)
    print("====================================")

    # Train Model
    model.fit(X_train, y_train)

    # Predict Values
    y_pred = model.predict(X_test)

    # ---------------------------------------------------
    # Evaluation Metrics
    # ---------------------------------------------------

    mae = mean_absolute_error(y_test, y_pred)

    mse = mean_squared_error(y_test, y_pred)

    rmse = np.sqrt(mse)

    r2 = r2_score(y_test, y_pred)

    # ---------------------------------------------------
    # Print Results
    # ---------------------------------------------------

    print("Mean Absolute Error (MAE) :", mae)

    print("Mean Squared Error (MSE) :", mse)

    print("Root Mean Squared Error (RMSE) :", rmse)

    print("R2 Score :", r2)

# ---------------------------------------------------
# End of Program
# ---------------------------------------------------