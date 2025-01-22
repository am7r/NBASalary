import pandas as pd

def processData(teamName):
    statsOne = f"data/{teamName}.csv"
    statsTwo = f"data/{teamName}2.csv"
    statsThree = f"data/{teamName}3.csv"
    salary = f"data/{teamName}Salary.csv"

    # Load data
    dataOne = pd.read_csv(statsOne)
    dataTwo = pd.read_csv(statsTwo)
    dataThree = pd.read_csv(statsThree)
    salaryData = pd.read_csv(salary)

    # Merge datasets
    mergeData = pd.merge(dataOne, dataTwo, on='Player')
    mergeData = pd.merge(mergeData, dataThree, on='Player')
    mergeData = pd.merge(mergeData, salaryData, on='Player', how='inner')


    # List of future salary columns to consider
    future_salary_columns = ['2024-25', '2025-26', '2026-27', '2027-28', '2028-29', '2029-30']

    # Add "yearsLeft" column (count columns with any non-NaN value)
    mergeData['yearsLeft'] = mergeData[future_salary_columns].apply(
        lambda row: row.notna().sum(), axis=1
    )

    # Drop all salary columns except "2024-25"
    columns_to_drop = [col for col in future_salary_columns if col != '2024-25']
    mergeData = mergeData.drop(columns=columns_to_drop, errors='ignore')

    # Drop additional unnecessary columns
    additional_columns_to_drop = ['Awards_y', 'Player-additional_y', 'Awards_x', 'Player-additional_x', 'Guaranteed', 'Rk_x', 'No', 'Ht', 'Wt', 'Birth Date', 'Birth', 'College']
    mergeData = mergeData.drop(columns=additional_columns_to_drop, errors='ignore')

    mergeData['2024-25'] = mergeData['2024-25'].replace(r'[\$,]', '', regex=True).astype(float)
    mergeData['2024-25'] = pd.to_numeric(mergeData['2024-25'], errors='coerce').fillna(0)


    # Save the processed data
    mergeData.to_csv(f"data/{teamName}MergedData.csv", index=False)
    print(f"Processed data saved to {teamName}MergedData.csv")

# Process the Warriors data
processData("Warriors")
