Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
from datetime import datetime, date
import re
import mysql.connector
import random

class nuser():

    def get_name(self):
        while True:
            name = input("Enter the name: ")
            if isinstance(name, str):
                if name.strip().isalpha():
                    print(f"Yours Name: {name}")
                    return name
                else:
                    print("Enter the correct name (letters only).")
            else:
                print("Enter the correct name (string expected).")

    def get_fname(self):
        while True:
            fname = input("Enter the father name: ")
            if isinstance(fname, str):
                if fname.strip().isalpha():
                    print(f"Father Name: {fname}")
                    return fname
                else:
                    print("Enter the correct name (letters only).")
            else:
                print("Enter the correct name (string expected).")

    def get_pno(self):
        while True:
            try:
                pno = int(input("Enter your 10-digit phone number: "))
                pno = abs(pno)
                phone_str = str(pno)
                if len(phone_str) == 10:
                    print("Phone number accepted:", phone_str)
                    return phone_str
                else:
                    print("Invalid! Phone number must be 10 digits.")
            except ValueError:
                print("Please enter only numbers.")

    def address(self):
        print("ADDRESS INFORMATION")
        address = {}
        address['house_no'] = input("Enter House/Flat No: ").strip()
        address['street'] = input("Enter Street/Area: ").strip()
        address['landmark'] = input("Enter Landmark (optional): ").strip()
        while True:
            city = input("Enter City: ").strip()
            if city and city.replace(" ", "").isalpha():
                address['city'] = city.title()
                break
            else:
                print("Please enter a valid city name")

        while True:
            state = input("Enter State: ").strip()
            if state and state.replace(" ", "").isalpha():
                address['state'] = state.title()
                break
            else:
                print("Please enter a valid state name")

        while True:
            pincode = input("Enter Pincode (6 digits): ").strip()
            if pincode.isdigit() and len(pincode) == 6:
                address['pincode'] = pincode
                break
            else:
                print("Please enter a valid 6-digit pincode")

        return address

    def get_dob(self):
        while True:
            try:
                dob_str = input('Enter your Date of Birth(dd - mm - yyyy):')
                dob = datetime.strptime(dob_str, '%d - %m - %Y').date()
                today = date.today()
                age = today.year - dob.year
                if (today.month, today.day) < (dob.month, dob.day):
                    age -= 1
                print(f"Your age is: {age}")
                if age >= 18:
                    print("Age accepted")
                    return dob
                else:
                    print("Not accepted (must be 18+). Please try again.")
            except ValueError:
                print("Invalid date format! Please enter in dd - mm - yyyy format.")

    def get_add(self):
        while True:
            addn = input("Enter your 12-digit Aadhaar number: ").strip()
            if not addn.isdigit():
                print("Invalid! Please enter only numbers.")
                continue
            if len(addn) == 12:
                print("Aadhaar number accepted:", addn)
                return addn
            else:
                print("Invalid! Aadhaar must be exactly 12 digits.")

    def get_pan(self):
        while True:
            pan = input("Enter PAN card number: ").strip().upper().replace(" ", "")
            if re.match(r'^[A-Z]{5}\d{4}[A-Z]$', pan):
                print(f"Valid PAN: {pan}")
                return pan
            else:
                print("Invalid PAN! Format: ABCDE1234F")

# Collect user data
user = nuser()
print("YOUR DETAILS")
name = user.get_name()
fname = user.get_fname()
pno = user.get_pno()
add = user.address()
dob = user.get_dob()
addn = user.get_add()
... pan = user.get_pan()
... 
... print("Do you want an ATM card?")
... print("1. Yes\n2. No")
... yorn = int(input("Select option: "))
... 
... if yorn == 1:
...     account_no = str(random.randint(10*11, (10*12) - 1))
...     print(f"YOUR ACCOUNT NUMBER: {account_no}")
... else:
...     account_no = None
... 
... # 🧠 MySQL Database Connection
... try:
...     conn = mysql.connector.connect(
...         host="localhost",
...         user="root",          # your MySQL username
...         password="raeva1511",          # your MySQL password
...         database="user_db"    # database name you created
...     )
...     cursor = conn.cursor()
... 
...     sql = """
...     INSERT INTO user_details 
...     (name, father_name, phone, house_no, street, landmark, city, state, pincode, dob, aadhaar, pan, account_no)
...     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
...     """
... 
...     val = (name, fname, pno, add['house_no'], add['street'], add['landmark'],
...            add['city'], add['state'], add['pincode'], dob, addn, pan, account_no)
... 
...     cursor.execute(sql, val)
...     conn.commit()
...     print("\n✅ User data saved successfully to MySQL Database!")
... 
... except mysql.connector.Error as err:
...     print(f"❌ Database Error: {err}")
... finally:
...     if conn.is_connected():
...         cursor.close()
