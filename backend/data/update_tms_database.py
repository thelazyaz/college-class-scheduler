import sqlite3
import csv

# Create table
connection = sqlite3.connect("backend/data/courses.db")
cursor = connection.cursor()
cursor.execute(f"CREATE TABLE courses (term TEXT, subject_code TEXT, course_number TEXT, instruction_type TEXT, instruction_method TEXT, section TEXT, crn_url TEXT, crn TEXT, course_title TEXT, days TEXT, times TEXT, instructor TEXT)")

terms = {
    "fall": "fall-tms.csv",
    "winter": "winter-tms.csv",
    "spring": "spring-tms.csv",
    "summer": "summer-tms.csv",
}

# One term at a time
with open('backend/data/fall-tms.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    for i, row in enumerate(spamreader):
        if (i == 0): continue
        # Split out data
        subject_code = row[0]
        course_number = row[1]
        instruction_type = row[2]
        instruction_method = row[3]
        section = row[4]
        crn_url = row[5]
        crn = row[6]
        course_title = row[7]
        days = row[8]
        times = row[9]
        instructor = row[10]

        # Insert table
        sql = "INSERT INTO courses VALUES ((?), (?), (?), (?), (?), (?), (?), (?), (?), (?), (?), (?))"
        cursor.execute(sql, ('fall', subject_code, course_number, instruction_type, instruction_method, section, crn_url, crn, course_title, days, times, instructor))

connection.commit()
connection.close()
