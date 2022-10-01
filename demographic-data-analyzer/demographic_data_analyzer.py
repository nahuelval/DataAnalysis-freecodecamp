import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = pd.Series(dtype='int64')
    race_count['White'] = len(df['race'][df['race'] == "White"])
    race_count['Black'] = len(df['race'][df['race'] == "Black"])

    j = 0

    for i in df['race'].unique():
        race_count.at[i] = len(df['race'][df['race'] == i])

    # What is the average age of men?
    average_age_men = round((df['age'][(df['sex'] == 'Male') | (df['sex'] == 'male')].mean()),1)

    # What is the percentage of people who have a Bachelor's degree?
    df_bachelors = len(df['education'][df['education'] == 'Bachelors'])
    percentage_bachelors = round((df_bachelors / len(df) * 100),1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    salary_find = ((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate'))
    educ_find = df['salary'].loc[salary_find & (df['salary'] == '>50K')]
    educ2_find = df['salary'].loc[salary_find]
    percentage_advanced_education = round((len(educ_find) / len(educ2_find) * 100),1)

    # What percentage of people without advanced education make more than 50K?
    educ_find2 = df['salary'].loc[~(salary_find) & (df['salary'] == '>50K')]
    educ2_find2 = df['salary'].loc[~(salary_find)]
    percentage_without_advanced_education = round((len(educ_find2) / len(educ2_find2) * 100),1)

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher = df['education'][(salary_find)]
    higher_education = round(len(higher),1)
    lower = df['education'][~(salary_find)]
    lower_education = round(len(lower),1)

    # percentage with salary >50K
    higher_rich = df['salary'].loc[(salary_find) & (df['salary'] == '>50K')]
    higher_education_rich = round((len(higher_rich) / len(higher) * 100),1)
    lower_rich = df['salary'].loc[~(salary_find) & (df['salary'] == '>50K')]
    lower_education_rich = round((len(lower_rich) / len(lower) * 100),1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_work = df[df['hours-per-week'] == min_work_hours]
    min_work_50k = min_work['salary'][min_work['salary'] == '>50K']
    rich_percentage = round((len(min_work_50k) / len(min_work) * 100),1)

    # What country has the highest percentage of people that earn >50K?
    df2 = pd.DataFrame({
    "country" : [],
    "percentage-50k" : []}, dtype=object)

    j = 0

    for i in df['native-country'].unique():
        df2.loc[j, 'country'] = i
        df2.loc[j, 'percentage-50k'] = round(len(df[(df['native-country'] == i) & (df['salary'] == ">50K")]) / len(df[(df['native-country'] == i)]) * 100,1)
        j = j+1

    df2['percentage-50k'] = pd.to_numeric(df2['percentage-50k'])

    index_salary50k = df2[df2['percentage-50k'] == df2['percentage-50k'].max()].index.values[0]

    highest_earning_country = df2.loc[index_salary50k,'country']
    highest_earning_country_percentage = round(df2['percentage-50k'].max(),1)

    # Identify the most popular occupation for those who earn >50K in India.
    
    df3 = pd.DataFrame({
    "occupation": [],
    "total-people": []
    })

    j = 0

    indian_salary50k = df['occupation'][(df['native-country'] == 'India') & (df['salary'] == '>50K')]

    for i in indian_salary50k.unique():
        df3.loc[j, 'occupation'] = i
        df3.loc[j, 'total-people'] = len(df['occupation'][(df['native-country'] == 'India') & (df['salary'] == '>50K') & (df['occupation'] == i)])
        j=j+1

    df3['total-people'] = pd.to_numeric(df3['total-people'])

    index_indian_rich = df3[df3['total-people'] == df3['total-people'].max()].index.values[0]

    top_IN_occupation = df3.loc[index_indian_rich,'occupation']

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
