# A Pandas DataFrame is a 2 dimensional data structure,
# like a 2 dimensional array, or a table with rows and columns.

import pandas as pd

student_data = {
    "Name": ["Prajun", "Swathi", "Gokul"],
    "Dept": ["Physics", "Mathematics", "Computer Science"]
}

df = pd.DataFrame(student_data)
print(df)
