
import sys
import pandas as pd
file_names = ["../vit_data.xlsx", "../min_data.xlsx", "../fat_data.xlsx",
              "../iron_data.xlsx", "../protein_data.xlsx", "../carbs_data.xlsx"]
if __name__ == "__main__":
    # Check if at least one argument (allergies) is provided
    if len(sys.argv) < 2:
        print("Error: Please provide at least one allergy to filter.")
        sys.exit(1)

    # Get allergies from the command-line arguments
    allergies = sys.argv[1].split(',')

# Iterate over each Excel file
for file_name in file_names:
    try:
        # Load the data from the Excel file
        df = pd.read_excel(file_name)

        # Check if any food from the allergy list is present in the "Food" column
        matching_foods = df[df['Food'].isin(allergies)]['Food'].tolist()

        # If matches are found, print the file name
        if matching_foods:

            file_check = file_name

            # Load the data from the Excel sheet

    except Exception as e:
        print(f"Error processing {file_name}: {str(e)}")
try:
    # Load the data from the Excel sheet
    df = pd.read_excel(file_check)

    # Remove any rows with missing values
    df = df.dropna()

    # Filter the dataframe to remove the foods with allergies
    for allergy in allergies:
        if allergy in df['Food'].values:
            df = df[df['Food'] != allergy]

    # Print the remaining foods and their carbohydrate amounts
    remaining_foods = list(df['Food'])
    print(remaining_foods, end="")

except Exception as e:
    print(f"Error in FoodFilter.py: {str(e)}")
    sys.exit(1)
# Note: Make sure to replace "food1", "food2", "food3" with your actual list of allergies
