import pandas as pd

df = pd.read_csv('student_marks_dataset.csv')


print("------First 5 marks data-------")
print(df.head())
marks_column = df['Marks']

average_marks = marks_column.mean()
max_marks = marks_column.max()
min_marks = marks_column.min()
count_marks = marks_column.count()
median_marks = marks_column.median()


print(f"Average marks : {average_marks}")
print(f"Max marks : {max_marks}")
print(f"Min marks : {min_marks}")
print(f"Count marks : {count_marks}")
print(f"Median marks : {median_marks}")