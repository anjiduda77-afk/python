import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample dataset (replace with your actual data)
data = {
    'waterfront': [0, 1, 0, 1, 0, 0, 1, 0, 1, 0],
    'price': [300000, 1200000, 350000, 1300000, 400000, 320000, 1250000, 310000, 1400000, 330000]
}
df = pd.DataFrame(data)

# Create boxplot
sns.boxplot(x='waterfront', y='price', data=df)
plt.title('House Prices by Waterfront View')
plt.xlabel('Waterfront (0 = No, 1 = Yes)')
plt.ylabel('Price')
plt.show()