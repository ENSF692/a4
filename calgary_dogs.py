# calgary_dogs.py
# @author: Bo Zheng Ma
# ENSF692 A4
# A terminal-based application for computing and printing statistics based on a dog breed.
import pandas as pd
import numpy as np

def main():
    df = pd.read_excel("CalgaryDogBreeds.xlsx")
    
    # Normalize the 'Breed' column for case-insensitive comparison
    df['Breed'] = df['Breed'].str.upper()

    # User entry, catches keyerrror if breed is not found in the data and prompts user to try it again
    while True:
        try:
            breed_input = input("Please enter a dog breed: ").strip().upper()
            
            # Check if the breed exists in the data
            if breed_input not in df['Breed'].values:
                raise KeyError("Dog breed not found in the data. Please try again.")
            break
        except KeyError as e:
            print(e)

    # FIlter the DataFrame for the selected breed
    breed_data = df[df['Breed'] == breed_input]
    
    # Calculate total registrations for the breed
    total_registrations = breed_data['Total'].sum()
    # Get unique years from the 'Year' column of this breed
    unique_years = breed_data['Year'].unique()
    # convert year to string
    years_as_strings = map(str, unique_years)
    # Join all the years into a single string separated by comma
    formatted_year_string = ', '.join(years_as_strings)
    print(f"The {breed_input} was found in the top breeds for years: {formatted_year_string}")    
    
    print(f"There have been {total_registrations} {breed_input} dogs registered total.")

    # Calculate annual percentagees
    total_per_year = breed_data.groupby('Year')['Total'].sum()
    total_registrations_all = df.groupby('Year')['Total'].sum()
    three_year_total = 0
    for year, total in total_per_year.items():
        percentage = (total / total_registrations_all.loc[year]) * 100
        print(f"The {breed_input} was {percentage:.6f}% of top breeds in {year}.")
        three_year_total += total

    # Calculate three-year percentage of total registrations
    overall_total = df['Total'].sum()
    three_year_percentage = (three_year_total / overall_total) * 100
    print(f"The {breed_input} was {three_year_percentage:.6f}% of top breeds across all years.")

    # Find most frequently appearing months for the breed
    month_counts = breed_data['Month'].value_counts()
    max_count = month_counts.max()  # This finds the maximum frequency of any month
    most_frequent_months = month_counts[month_counts == max_count].index.tolist()  # This filters all months that have the maximum frequency
    print("Most frequently appearing month(s) for", breed_input, "dogs: ", " ".join(most_frequent_months))

if __name__ == '__main__':
    main()
