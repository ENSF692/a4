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

    # User entry, catches keyerrror if breed is not found
    while True:
        try:
            breed_input = input("Please enter a dog breed: ").strip().upper()
            
            # Check if the breed exists in the data
            if breed_input not in df['Breed'].values:
                raise KeyError("Dog breed not found in the data. Please try again.")
            break
        except KeyError as e:
            print(e)


if __name__ == '__main__':
    main()
