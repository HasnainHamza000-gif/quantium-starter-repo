import pandas as pd
import glob

# Step 1: Find all CSV files in the data folder
files = glob.glob('data/*.csv')

dfs = []

for file in files:
    df = pd.read_csv(file)

    # Step 2: Keep only 'pink morsel' rows
    df = df[df['product'] == 'pink morsel']

    # Step 3: Clean the price column (remove '$') and convert to float
    df['price'] = df['price'].astype(str).str.replace('$', '', regex=False).astype(float)

    # Step 4: Calculate total sales
    df['sales'] = df['quantity'] * df['price']

    # Step 5: Keep only required columns
    df = df[['sales', 'date', 'region']]

    dfs.append(df)

# Step 6: Combine all dataframes into one
final_df = pd.concat(dfs, ignore_index=True)

# Step 7: Save to output CSV file
final_df.to_csv('formatted_data.csv', index=False)

print("Data processing complete! 'formatted_data.csv' has been generated.")