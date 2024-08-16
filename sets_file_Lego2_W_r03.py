import pandas as pd

# Load the CSV file into a DataFrame
file_path = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0078__Day74_Aggregate_and_Merge_Data_w_Pandas__240814\NewProject\r00-r09 START\r00_env_START\data\sets.csv'
df = pd.read_csv(file_path)

# Find the lowest year in the 'year' column
lowest_year = df['year'].min()

# Get the top 5 sets with the highest number of parts
top_5_sets = df.nlargest(5, 'num_parts')

# Count the total number of products sold in the lowest year
total_products_sold = df[df['year'] == lowest_year]['set_num'].count()

# Get the names of all sets in the lowest year
sets_in_lowest_year = df[df['year'] == lowest_year][['set_num', 'name']]

# Print the head and tail of the entire DataFrame
print("Head of the entire DataFrame:")
print(df.head())
print("\nTail of the entire DataFrame:")
print(df.tail())

# Print the results
print(f"\nThe lowest year in the dataset is: {lowest_year}")
print(f"The total number of products sold in {lowest_year} is: {total_products_sold}")

# Print the head and tail of the DataFrame filtered by the lowest year
print("\nHead of the sets in the lowest year:")
print(sets_in_lowest_year.head())
print("\nTail of the sets in the lowest year:")
print(sets_in_lowest_year.tail())

# Print the top 5 sets with the highest number of parts
print("\nTop 5 LEGO sets with the highest number of parts:")
print(top_5_sets[['set_num', 'name', 'num_parts']])
