import sqlite3

con = sqlite3.connect('hospitalDB.db')

cursor = con.cursor()


# sqlite_query = '''CREATE TABLE PatientDetails(
#                   patientCode INTEGER PRIMARY KEY,
#                   name TEXT NOT NULL,
#                   address TEXT NOT NULL,
#                   phone TEXT NOT NULL);'''
# cursor.execute(sqlite_query)
# print('table is created successfully')


def Add_Patient():
    Patient_Code = input("Enter Patient Code : ")
    Patient_Name = input("Enter Patient Name : ")
    Patient_Address = input("Enter Patient's Address : ")
    Phone_no = input("Enter Patient's phone no. : ")
    data = (Patient_Code, Patient_Name, Patient_Address, Phone_no)

    insert_query = '''INSERT INTO PatientDetails
                             VALUES (?,?,?,?)'''

    cursor.execute(insert_query, data)

    con.commit()

    print("Patient's data Added Successfully\n ")
    menu()


def Display_All_Patients():
    sqlite_select_query = '''SELECT * FROM PatientDetails'''

    cursor.execute(sqlite_select_query)

    records = cursor.fetchall()
    print(records)

    for row in records:
        print('Patient_Code: ', row[0])
        print('Name: ', row[1])
        print('Address: ', row[2])
        print('Phone_No: ', row[3])
        print("------------------------")

    # con.close()

    menu()


def menu():
    print("\nPress ")
    print("1 for Adding Paitent")
    print("2 for View All Paitent Details ")
    print("3 for Exit")

    ch = int(input("Select Option: "))
    if ch == 1:
        Add_Patient()
    elif ch == 2:
        Display_All_Patients()
    elif ch == 3:
        exit(0)
    else:
        print("Invalid Choice")
        menu()


menu()