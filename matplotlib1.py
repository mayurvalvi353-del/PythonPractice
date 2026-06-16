import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
sales = [45,52,48,61,58,72,69,75,68,82,90,95]

#Line Chart
plt.figure(figsize=(12,5))
plt.plot(months, sales, marker = 'o', color = 'blue', linewidth = 2, markersize = 8)
plt.fill_between(months, sales, alpha = 0.15, color = 'green')
plt.title('Monthly Sales 2024 (Rs. Thousands)', fontsize = 14, fontweight = 'bold')
plt.xlabel('Month')
plt.ylabel('Sales (Rs. K)')
plt.grid(True, alpha = 0.3)
plt.tight_layout()
plt.show()

#Bar Chart
cities = ['Mumbai', 'Pune', 'Nashik', 'Nagpur', 'Satara', 'Kolhapur']
students = [1200, 2300, 1073, 980, 730, 345]
colors = ['#a8a232', '#a86832', '#52a832', '#329ea8', '#5a32a8', '#a83277']

plt.figure(figsize = (9,5))
bars = plt.bar(cities, students, color = colors, edgecolor = 'white', linewidth = 1.5)
plt.title('Students Enrolled per City')
plt.ylabel('Numberof Students')
plt.xlabel('Cities')
for bar, val in zip(bars, students) :
    plt.text(bar.get_x()+bar.get_width()/2, val+30, str(val), ha = 'center', fontweight = 'bold')
plt.tight_layout()
plt.show()

#Scatter Plot
import numpy as np
study_hrs = np.random.uniform(2,10,50)
marks = study_hrs * 7 + np.random.normal(0,8,50)
marks = np.clip(marks, 30, 100)

plt.figure(figsize = (8,5))
plt.scatter(study_hrs, marks, c = marks, cmap = 'plasma', s = 100, alpha = 0.8)
plt.colorbar(label = 'Marks')
plt.title('Study Hours vs Exam Marks')
plt.xlabel('Study Hours/Day')
plt.ylabel('Exam Marks')
plt.show()