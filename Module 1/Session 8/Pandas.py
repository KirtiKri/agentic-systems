import pandas as pd

df = pd.read_csv('data.csv')

#Structure and inspection: print df.shape, df.head(3), and df.info(). In one or two sentences, state what info() reveals about missing values in this dataset.
print(f"df_shaped {df.shape}")
print(f"df_head {df.head(3)}")
print(df.info())
#info() shows the number of non-null values in each columns

#Boolean indexing: build df_ny — rows where city equals 'New York' (use the actual column name from the file).
df['city'] = df['city'].str.strip()
df_ny = df['city'] == 'New York'
print("df_ny")
print(df[df_ny])

#Compound condition: build df_high — rows where amount is present and amount > 60 (use & and parentheses as needed).
df_high= (df['amount'].notna()) & (df['amount']> 60)
print("df_high")
print(df[df_high])

#Sorting and index: build df_sorted — sort by amount descending, put missing amount first via na_position, then apply reset_index(drop=True).
df_sorted = df.sort_values(by= 'amount', ascending= False, na_position= 'first').reset_index(drop= True)
print("df_sorted")
print(df_sorted)


#Missing values — detection and handling:
#Report per-column missing counts with isna().sum().
print("per-column missing counts ")
print(df.isna().sum())

#Build df_imputed: copy df; replace missing amount with the mean of amount (computed from non-null values); replace missing city with the string 'Unknown'.
df_imputed = df.copy()
avg = df_imputed['amount'].mean()
print(f"Average :{avg}")
df_imputed['amount'] = df_imputed['amount'].fillna(avg)
df_imputed['city'] = df_imputed['city'].fillna('Unknown')
print("df_imputed")
print(df_imputed)

#Build df_dropped: starting from df, drop rows that have a missing amount using dropna with an appropriate subset.
df_dropped = df.dropna(subset= ['amount'])
print("df_dropped")
print(df_dropped)