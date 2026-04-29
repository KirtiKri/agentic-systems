#Python 3.14.3 
#pip install pandas
#pyhton project_tracker.py
#Import pandas as pd.
import pandas as pd

#Create projects exactly as above.
projects = pd.DataFrame({
    "ProjectID":   ["P01", "P02", "P03", "P04", "P05", "P06"],
    "City":        ["Pune", "Pune", "Mumbai", "Mumbai", "Mumbai", "Nashik"],
    "ProjectName": ["Water", "Lights", "Clinic", "School", "Garden", "Skills"],
    "Budget_Lakh": [12.5, 8.0, 25.0, 18.5, 6.0, 9.5],
    "Volunteers":  [10, 14, 22, 30, 8, 12],
    "internal_only": ["x", "x", "x", "x", "x", "x"],   # junk — remove
    "legacy_flag":   [0, 0, 0, 0, 0, 0],                 # junk — remove
})

#Drop columns internal_only and legacy_flag using axis=1, and assign the result back so the working DataFrame has no junk columns.
projects = projects.drop("internal_only", axis=1)
projects = projects.drop("legacy_flag", axis=1)
print(projects)

#Build report with named aggregation using these exact output names: Num_Projects, Total_Budget_Lakh, Avg_Volunteers.
report = projects.groupby("City").agg(
    Num_Projects = ("ProjectID", "count"),
    Total_Budget_Lakh = ("Budget_Lakh", "sum"),
    Avg_Volunteers = ("Volunteers", "mean")
)

#Print a short banner line (e.g. NGO summary by city) and print report.
print("-------NGO summary by city--------")
print(report)

#(Stretch, optional) Call .reset_index() on a copy of the report and print it once, so City appears as a normal column.
old = report.reset_index()
print(old)