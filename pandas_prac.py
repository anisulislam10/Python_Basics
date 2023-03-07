import numpy as np
import pandas as pd
Student_information_DB = {
    "Student_Name": ['Anisul Islam', 'Hashmat Ullah', 'Bilal Shah'],
    "Student_regNo": [3250, 3247, 3344],
    "Student_Program": ["BSSE", "BSSE", "BSCS"],
    "Student_Semester": ["8th", "7th", "8th"],
    "Student_CGPA": [3.66, 2.1, 1.98]
}
df = pd.DataFrame(Student_information_DB)
print(df)
