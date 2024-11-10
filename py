# Make a variable for the column names with year numbers
years = ['2024', '2023', '2022', '2021']

# Drop columns with year numbers greater than `2021`
df_t = df_t.drop(columns=[year for year in df_t.columns if year not in years])

# Reset index and rename it to `year`
df_t = df_t.reset_index().rename(columns={'index': 'year'})

# Melt the dataframe using `year` as the identifier variable
melted_df = df_t.melt(id_vars='year', value_vars=years)

# Convert `year` to numeric
melted_df['year'] = pd.to_numeric(melted_df['year'])

# Drop rows with null values
melted_df = melted_df.dropna()

# Display the first 5 rows
print(melted_df.head().to_markdown(index=False, numalign="left", stralign="left"))

# Print the column names and their data types
print(melted_df.info())
