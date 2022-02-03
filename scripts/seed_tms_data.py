import sqlite3
import csv

with open('../data/tms_data.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        # Split out data
        subject_code = row[0]
        course_number = row[1]
        instruction_type = row[2]
        instruction_method = row[3]
        section = row[4]
        crn_url = row[6]
        crn = row[7]
        course_title = row[8]
        days = row[9]
        times = row[10]
        finals_day = row[11]
        finals_time = row[12]
        instructor = row[13]

        # Create table
        connection = sqlite3.connect("courses.db")
        cursor = connection.cursor()
        cursor.execute(f"CREATE TABLE courses (subject_code TEXT, course_number TEXT, instruction_type TEXT, instruction_method TEXT, section TEXT, crn_url TEXT, crn TEXT, course_title TEXT, days TEXT, times TEXT, finals_day TEXT, finals_time TEXT, instructor TEXT)")

        # Insert table
        cursor.execute(f"INSERT INTO courses VALUES ('{subject_code}', '{course_number}', '{instruction_type}', '{instruction_method}', '{section}', '{crn_url}', '{crn}', '{course_title}', '{days}', '{times}', '{finals_day}', '{finals_time}', '{instructor}')")
        conn.commit()
        conn.close()
