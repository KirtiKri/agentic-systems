import pandas as pd

orders = pd.DataFrame({
    "OrderID":        [101, 102, 103, 104, 105, 106],
    "RestaurantID":   ["R01", "R02", "R01", "R03", "R02", "R04"],
    "CustomerName":   ["Ananya", "Rohit", "Priya", "Dev", "Sara", "Meera"],
    "Amount":         [450, 320, 560, 180, 290, 720]
})

restaurants = pd.DataFrame({
    "RestaurantID":   ["R01", "R02", "R03", "R05"],
    "RestaurantName": ["Spice Garden", "The Grill House", "Curry Corner", "Pasta Palace"],
    "City":           ["Delhi", "Mumbai", "Delhi", "Bengaluru"]
})
#Step 1 — Merge the DataFrames
#Print the merged DataFrame and state in a comment which join type you used and why.
new_table = pd.merge(orders, restaurants, on="RestaurantID", how = "inner")
print(new_table)
#we used the inner merge type so that the RestaurantID that doesn't exist in both  tables gets excluded

#Step 2 — Clean the Merged Result
#Drop the RestaurantID column (it is no longer needed after the merge)
new_table = new_table.drop(columns= ["RestaurantID"])
#Rename the following columns:
#"Amount" → "Revenue"
#"RestaurantName" → "Restaurant"
new_table = new_table.rename(columns= {
    "Amount" : "Revenue",
    "RestaurantName" : "Restaurant"
})

print(new_table)

#Step 3 — Build the City-Wise Report Using a Single Pipeline
city_report = (pd.merge(orders, restaurants, on = "RestaurantID", how="inner")
               .groupby("City")
               .agg(
                    Total_Revenue =("Amount", "sum"),
                    Order_Count = ("OrderID", "count")
                   )
               .reset_index()
               .sort_values(by = "Total_Revenue", ascending = False)
)
print(city_report)

#Step 4 — Interpret the Output
#Which city generated the highest total revenue, and what was the amount?
#Delhi generated the highest revenue, 1190

#Why does Pasta Palace (R05, Bengaluru) not appear in the report?
#This is because we used inner merge, as "R05" exists only in Restaurant Table and not in Orders Table, it got excluded

#Why does Order 106 (R04) not appear in the report?
#Again RestaurantID R04 is present in the orders table but not in the Restaurant table, thus got excluded in inner merge