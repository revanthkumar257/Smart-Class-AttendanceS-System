import os
import datetime

def mark_attendence(self, student_id, name, department):
    file_path = "attendance.csv"

    # Ensure the file exists before reading
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write("Student_ID,Name,Department,Time,Date,Status\n")

    # Open the file in append mode
    with open(file_path, "a+", newline="\n") as f:
        f.seek(0)
        myDataList = f.readlines()
        name_list = [entry.split(",")[0] for entry in myDataList]

        if student_id not in name_list:
            now = datetime.now()
            date_str = now.strftime("%d/%m/%Y")
            time_str = now.strftime("%H:%M:%S")
            f.write(f"{student_id},{name},{department},{time_str},{date_str},Present\n")

import os

file_path = "attendance.csv"

# Ensure the file is created
if not os.path.exists(file_path):
    print(f"❌ File '{file_path}' is missing. Creating a new one...")
    with open(file_path, "w") as f:
        f.write("Student_ID,Name,Department,Time,Date,Status\n")
        print(f"✅ File '{file_path}' created successfully.")
else:
    print(f"✅ File '{file_path}' already exists.")
