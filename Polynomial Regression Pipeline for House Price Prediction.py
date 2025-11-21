import pandas as pd
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import r2_score

# Sample dataset (replace with your actual data)
data = {
    'floors': [1, 2, 1, 2, 1],
    'waterfront': [0, 1, 0, 1, 0],
    'lat': [47.5, 47.6, 47.7, 47.6, 47.5],
    'bedrooms': [3, 4, 2, 5, 3],
    'sqft_basement': [0, 500, 0, 600, 0],
    'view': [0, 3, 0, 4, 0],
    'bathrooms': [1.5, 2.5, 1.0, 3.0, 2.0],
    'sqft_living15': [1500, 2500, 1300, 2700, 1600],
    'sqft_above': [1500, 2000, 1300, 2100, 1600],
    'grade': [7, 9, 6, 10, 8],
    'sqft_living': [1800, 2500, 1500, 2700, 1900],
    'price': [400000, 850000, 350000, 950000, 450000]
}
df = pd.DataFrame(data)

# Features and target
features = ['floors', 'waterfront', 'lat', 'bedrooms', 'sqft_basement', 'view',
            'bathrooms', 'sqft_living15', 'sqft_above', 'grade', 'sqft_living']
X = df[features]
y = df['price']

# Create pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('poly', PolynomialFeatures(degree=2)),
    ('model', LinearRegression())
])

# Fit and evaluate
pipeline.fit(X, y)
r2 = pipeline.score(X, y)
print("R² score:", r2)