from pathlib import Path
from typing import Any

import pandas as pd


HIGH_INCOME = '>50K'
ADVANCED_EDUCATION = {'Bachelors', 'Masters', 'Doctorate'}


def calculate_demographic_data(print_data: bool = True) -> dict[str, Any]:
    """Calculate demographic statistics from the bundled Census dataset.

    Args:
        print_data: When true, print a readable summary of the results.

    Returns:
        A dictionary containing the calculated pandas Series and scalar values.
    """
    data_file = Path(__file__).with_name('adult.data.csv')
    df = pd.read_csv(data_file, skipinitialspace=True)

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df.loc[df['sex'] == 'Male', 'age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # Separate people with advanced education from everyone else.
    higher_education = df['education'].isin(ADVANCED_EDUCATION)
    lower_education = ~higher_education

    higher_education_rich = round(
        (df.loc[higher_education, 'salary'] == HIGH_INCOME).mean() * 100, 1
    )
    lower_education_rich = round(
        (df.loc[lower_education, 'salary'] == HIGH_INCOME).mean() * 100, 1
    )

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df['hours-per-week'] == min_work_hours

    rich_percentage = round(
        (df.loc[num_min_workers, 'salary'] == HIGH_INCOME).mean() * 100, 1
    )

    # What country has the highest percentage of people that earn >50K?
    country_percentages = (
        df.groupby('native-country')['salary']
        .apply(lambda salaries: (salaries == HIGH_INCOME).mean() * 100)
    )
    highest_earning_country = country_percentages.idxmax()
    highest_earning_country_percentage = round(country_percentages.max(), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_india_occupation = (
        df.loc[
            (df['native-country'] == 'India') & (df['salary'] == HIGH_INCOME),
            'occupation',
        ]
        .value_counts()
        .idxmax()
    )

    if print_data:
        print('Number of each race:\n', race_count)
        print('Average age of men:', average_age_men)
        print(f'Percentage with Bachelors degrees: {percentage_bachelors}%')
        print(f'Percentage with higher education that earn >50K: {higher_education_rich}%')
        print(f'Percentage without higher education that earn >50K: {lower_education_rich}%')
        print(f'Min work time: {min_work_hours} hours/week')
        print(f'Percentage of rich among those who work fewest hours: {rich_percentage}%')
        print('Country with highest percentage of rich:', highest_earning_country)
        print(f'Highest percentage of rich people in country: {highest_earning_country_percentage}%')
        print('Top occupations in India:', top_india_occupation)

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
        'top_IN_occupation': top_india_occupation,
    }
