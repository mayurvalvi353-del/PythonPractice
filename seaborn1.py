import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

df = pd.DataFrame({
    'marks' : np.random.randint(40,100,100),
    'study_hours' : np.random.uniform(2,10,100),
    'city': np.random.choice(['Bhopal','Indore','Jabalpur'],100),
    'gender' : np.random.choice(['Male','Female'],100)
})

plt.figure(figsize = (10,4))
sns.histplot(df['marks'], bins = 20, kde = True, color = 'silver')
plt.title('Distribution of Student Marks')
plt.show()
