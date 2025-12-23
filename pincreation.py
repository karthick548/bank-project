import pymysql

def create_account():
    try:
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="raeva1511",
            database="user_db"
        )
        cursor = conn.cursor()

        while True:
            acc_no = input("Enter your Account Number (12 digits): ").strip()
            if not acc_no.isdigit() or not (12 == len(acc_no)):
                print(" Invalid format! Must be 12 digits.")
                continue

            cursor.execute("SELECT * FROM user_details WHERE account_no = %s", (acc_no,))
            result = cursor.fetchone()
            if result:
                print(" Account number found.")
                break
            else:
                print(" Account number not found. Please try again.")

        while True:
            pin = input("Set your 4-digit PIN: ").strip()
            if pin.isdigit() and len(pin) == 4:
                confirm_pin = input("Confirm your PIN: ").strip()
                if pin == confirm_pin:
                    print(" PIN set successfully.")
                    break
                else:
                    print(" PINs do not match. Try again.")
            else:
                print(" Invalid PIN! Must be exactly 4 digits.")

        try:
            cursor.execute(
                "INSERT INTO account_credentials (account_no, pin) VALUES (%s, %s)",
                (acc_no, pin)
            )
            conn.commit()
            print(f"\n PIN saved successfully for Account: {acc_no}")
        except pymysql.IntegrityError:
            print("⚠ PIN already exists for this account. Cannot create again.")

        return acc_no, pin

    except pymysql.MySQLError as e:
        print(f" Database Error: {e}")
        return None, None
    finally:
        if conn:
            cursor.close()
            conn.close()


account, pin = create_account()

if account and pin:
    print(f"\n Account {account} is now secured with your PIN.")
