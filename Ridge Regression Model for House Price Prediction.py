import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# Sample dataset (replace with your actual data)
data = {
    'floors': [1, 2, 1, 2, 1, 2, 1, 2],
    'waterfront': [0, 1, 0, 1, 0, 1, 0, 1],
    'lat': [47.5, 47.6, 47.7, 47.6, 47.5, 47.6, 47.7, 47.6],
    'bedrooms': [3, 4, 2, 5, 3, 4, 2, 5],
    'sqft_basement': [0, 500, 0, 600, 0, 500, 0, 600],
    'view': [0, 3, 0, 4, 0, 3, 0, 4],
    'bathrooms': [1.5, 2.5, 1.0, 3.0, 2.0, 2.5, 1.0, 3.0],
    'sqft_living15': [1500, 2500, 1300, 2700, 1600, 2500, 1300, 2700],
    'sqft_above': [1500, 2000, 1300, 2100, 1600, 2000, 1300, 2100],
    'grade': [7, 9, 6, 10, 8, 9, 6, 10],
    'sqft_living': [1800, 2500, 1500, 2700, 1900, 2500, 1500, 2700],
    'price': [400000, 850000, 350000, 950000, 450000, 850000, 350000, 950000]
}
df = pd.DataFrame(data)

# Features and target
features = ['floors', 'waterfront', 'lat', 'bedrooms', 'sqft_basement', 'view',
            'bathrooms', 'sqft_living15', 'sqft_above', 'grade', 'sqft_living']
X = df[features]
y = df['price']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Fit Ridge regression
ridge_model = Ridge(alpha=0.1)
ridge_model.fit(X_train, y_train)

# Evaluate