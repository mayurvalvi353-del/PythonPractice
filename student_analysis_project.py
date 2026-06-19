import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

try:
    df = pd.read_csv("students_marks.csv")
except FileNotFoundError:
    print("File not found!")
    exit()

numeric_cols = [
    "Maths",
    "Science",
    "English",
    "History",
    "Computer"
]

for col in numeric_cols:
    df[col] = df[col].fillna(df[col].mean())

df["City"] = df["City"].fillna("Unknown")


df["Total"] = df[numeric_cols].sum(axis=1)

df["Average"] = df["Total"] / 5

def get_grade(avg):

    if avg >= 90:
        return "A+"

    elif avg >= 80:
        return "A"

    elif avg >= 70:
        return "B"

    elif avg >= 60:
        return "C"

    else:
        return "F"

df["Grade"] = df["Average"].apply(get_grade)

df["Rank"] = df["Total"].rank(
    ascending=False,
    method="dense"
).astype(int)

print("\n===== SUMMARY =====")

class_average = df["Average"].mean()

print("Class Average :", round(class_average, 2))

topper = df.loc[df["Total"].idxmax()]

print("Topper :", topper["Name"])

failure_rate = (
    len(df[df["Grade"] == "F"])
    / len(df)
) * 100

print("Failure Rate :", round(failure_rate, 2), "%")

print("\nCity Wise Average:")

city_avg = (
    df.groupby("City")["Average"]
    .mean()
    .round(2)
)

print(city_avg)

report = {
    "Class Average":[round(class_average,2)],
    "Topper":[topper["Name"]],
    "Failure Rate":[round(failure_rate,2)]
}

report_df = pd.DataFrame(report)

report_df.to_csv(
    "report.csv",
    index=False
)
 #Bar Chart of Average marks per city 
plt.figure(figsize=(8,5))

city_avg.plot(kind="bar")

plt.title("City Average Marks")
plt.ylabel("Average")

plt.tight_layout()
plt.show()

#Pie Chart
grade_counts = df["Grade"].value_counts()

plt.figure(figsize=(6,6))

plt.pie(
    grade_counts,
    labels=grade_counts.index,
    autopct="%1.1f%%"
)

plt.title("Grade Distribution")


plt.show()

#Scatter Plot
plt.figure(figsize=(8,5))

plt.scatter(
    df["Study_Hours"],
    df["Average"]
)

plt.xlabel("Study Hours")

plt.ylabel("Average Marks")

plt.title("Study Hours vs Marks")

plt.savefig(
    "charts/study_vs_marks.png"
)

plt.show()

#Line Chart
rank_df = df.sort_values("Rank")

plt.figure(figsize=(8,5))

plt.plot(
    rank_df["Rank"],
    rank_df["Total"]
)

plt.xlabel("Rank")

plt.ylabel("Total Marks")

plt.title("Rank vs Score")

plt.savefig(
    "charts/rank_vs_score.png"
)

plt.show()

#Correlation Heatmap
plt.figure(figsize=(8,6))

sns.heatmap(
    df[numeric_cols].corr(),
    annot=True
)

plt.title(
    "Subject Correlation Heatmap"
)

plt.savefig(
    "charts/subject_correlation.png"
)

plt.show()

print("\nProject Completed Successfully!")

