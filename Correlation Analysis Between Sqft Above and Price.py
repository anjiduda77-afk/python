# Creating and evaluating a linear regression model for house price prediction using sqft_living
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Generate a sample dataset
np.random.seed(42)
sqft_living = np.random.randint(500, 4500, 100)
price = sqft_living * 300 + np.random.normal(0, 50000, 100)  # adding noise

# Create DataFrame
df = pd.DataFrame({
    'sqft_living': sqft_living,
    'price': price
})

# Split data into training and testing sets
X = df[['sqft_living']]
y = df['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict and calculate R^2 score
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)

# Plot the regression line
plt.style.use('seaborn-v0_8')
plt.figure(figsize=(8, 6))
plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Predicted')
plt.xlabel('sqft_living')
plt.ylabel('price')
plt.title('Linear Regression: Price vs Sqft Living')
plt.legend()
plt.tight_layout()
plt.savefig('/mnt/data/price_vs_sqft_living.png')

# Print R^2 score
print(f"R^2 Score: {r2:.4f}")