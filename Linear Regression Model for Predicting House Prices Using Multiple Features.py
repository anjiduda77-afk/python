# Creating and evaluating a linear regression model for house price prediction
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

# Generate a sample dataset
np.random.seed(42)
n_samples = 500
data = {
    'floors': np.random.randint(1, 4, n_samples),
    'waterfront': np.random.randint(0, 2, n_samples),
    'lat': np.random.uniform(47.0, 47.8, n_samples),
    'bedrooms': np.random.randint(1, 6, n_samples),
    'sqft_basement': np.random.randint(0, 1000, n_samples),
    'view': np.random.randint(0, 5, n_samples),
    'bathrooms': np.random.uniform(1, 4, n_samples),
    'sqft_living15': np.random.randint(500, 3000, n_samples),
    'sqft_above': np.random.randint(500, 3000, n_samples),
    'grade': np.random.randint(1, 13, n_samples),
    'sqft_living': np.random.randint(500, 3000, n_samples),
}

# Simulate house prices with some noise
data['price'] = (
    50000 +
    data['floors'] * 10000 +
    data['waterfront'] * 50000 +
    data['lat'] * 1000 +
    data['bedrooms'] * 8000 +
    data['sqft_basement'] * 20 +
    data['view'] * 15000 +
    data['bathrooms'] * 12000 +
    data['sqft_living15'] * 30 +
    data['sqft_above'] * 25 +
    data['grade'] * 20000 +
    data['sqft_living'] * 35 +
    np.random.normal(0, 50000, n_samples)
)

df = pd.DataFrame(data)

# Define features and target
features = ['floors', 'waterfront', 'lat', 'bedrooms', 'sqft_basement', 'view',
            'bathrooms', 'sqft_living15', 'sqft_above', 'grade', 'sqft_living']
target = 'price'

X = df[features]
y = df[target]

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)

print(f"R^2 Score of the Linear Regression Model: {r2:.4f}")