# Demographic Data Analyzer

This project analyzes the U.S. Census Income dataset with pandas. It calculates
demographic distributions, education and income comparisons, work-hour
statistics, and country-level income results.

## Requirements

- Python 3.9 or newer
- pandas (listed in `requirements.txt`)

## Setup

Create and activate a virtual environment, then install the dependency:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Usage

Run the analyzer and its tests through the project entry point:

```bash
python main.py
```

To use the analyzer from another Python module:

```python
from demographic_data_analyzer import calculate_demographic_data

results = calculate_demographic_data(print_data=False)
print(results['highest_earning_country'])
```

The function returns a dictionary with the following keys:

- `race_count`: number of people in each race
- `average_age_men`: average age of men
- `percentage_bachelors`: percentage with a Bachelor's degree
- `higher_education_rich`: high-income percentage among people with advanced education
- `lower_education_rich`: high-income percentage among people without advanced education
- `min_work_hours`: minimum reported hours worked per week
- `rich_percentage`: high-income percentage among people working the minimum hours
- `highest_earning_country`: country with the highest high-income percentage
- `highest_earning_country_percentage`: that country's high-income percentage
- `top_IN_occupation`: most common occupation among high-income workers in India

## Project Files

- `demographic_data_analyzer.py`: analysis implementation
- `adult.data.csv`: source dataset
- `test_module.py`: automated tests for all required results
- `main.py`: development entry point
