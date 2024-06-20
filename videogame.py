import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')
csv_reader = pd.read_csv(r'C:\Users\37229\OneDrive\Desktop\Projects\top10.csv')
sns.barplot(x = 'Global_Sales', y = 'Name', data = csv_reader, palette = "Blues_d")
plt.xlabel('Global Sales (in millions)')
plt.ylabel('Video Games')
plt.title('Top 10 Video Games by Global Sales')
plt.tight_layout()
plt.savefig('VideoGame.png')
plt.show()
