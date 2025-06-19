import pandas as pd

df = pd.read_csv(r"C:\Users\lenovo\Desktop\Python\PYTHON_PROJECT\adult.csv")
print(df.head(3))

race_count = df['race'].value_counts()

average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

bachelors_percentage = round((df['education'] == 'Bachelors').mean() * 100, 1)

higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
lower_education = higher_education

higher_education_rich = round((df[higher_education]['salary'] == '>50K').mean() * 100, 1)
lower_education_rich = round((df[lower_education]['salary'] == '>50K').mean() * 100, 1)

min_work_hours = df['hours-per-week'].min()

rich_min_workers = df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')]
rich_percentage = round((len(rich_min_workers) / len(df[df['hours-per-week'] == min_work_hours])) * 100, 1)

rich_by_country = df[df['salary'] == '>50K']['native-country'].value_counts()
total_by_country = df['native-country'].value_counts()
rich_percentage_country = (rich_by_country / total_by_country * 100).dropna()
highest_earning_country = rich_percentage_country.idxmax()
highest_earning_country_percentage = round(rich_percentage_country.max(), 1)

top_occupation_in_india = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

print("Race Count:\n", race_count)
print("Average age of men:", average_age_men)
print("Percentage with Bachelors degrees:", bachelors_percentage)
print("Higher education rich:", higher_education_rich)
print("Lower education rich:", lower_education_rich)
print("Minimum work hours:", min_work_hours)
print("Rich percentage of min workers:", rich_percentage)
print("Highest earning country:", highest_earning_country)
print("Highest earning country percentage:", highest_earning_country_percentage)
print("Top occupation in India among rich:", top_occupation_in_india)