import pymysql

def connect_db():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="raeva1511",  
        database="user_db"
    )

def login():
    while True:
        acc_no = input("Enter your account number: ").strip()
        pin = input("Enter your 4-digit PIN: ").strip()

        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM account_credentials WHERE account_no=%s AND pin=%s", (acc_no, pin))
            result = cursor.fetchone()
            if result:
                print(" Login successful.")
                return acc_no
            else:
                print(" Invalid account or PIN. Try again.")
        except pymysql.MySQLError as e:
            print(" Database error:", e)
        finally:
            cursor.close()
            conn.close()

def initialize_balance(account_no):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM account_balance WHERE account_no = %s", (account_no,))
    result = cursor.fetchone()
    if not result:
        cursor.execute("INSERT INTO account_balance (account_no, balance) VALUES (%s, %s)", (account_no, 0))
        conn.commit()
    cursor.close()
    conn.close()

def get_balance(account_no):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM account_balance WHERE account_no = %s", (account_no,))
    balance = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return balance

def update_balance(account_no, new_balance):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE account_balance SET balance = %s WHERE account_no = %s", (new_balance, account_no))
    conn.commit()
    cursor.close()
    conn.close()

def deposit(account_no):
    amount = input("Enter deposit amount: ").strip()
    if not amount.isdigit():
        print(" Invalid amount.")
        return
    amount = abs(int(amount))
    current = get_balance(account_no)
    new_balance = current + amount
    update_balance(account_no, new_balance)
    print(f" ₹{amount} deposited. New balance: ₹{new_balance}")

def withdraw(account_no):
    amount = input("Enter withdrawal amount: ").strip()
    if not amount.isdigit():
        print(" Invalid amount.")
        return
    amount = abs(int(amount))
    current = get_balance(account_no)
    if amount > current:
        print(" Insufficient balance.")
    else:
        new_balance = current - amount
        update_balance(account_no, new_balance)
        print(f" ₹{amount} withdrawn. Remaining balance: ₹{new_balance}")

def balance_check(account_no):
    balance = get_balance(account_no)
    print(f" Current Balance: ₹{balance}")

def main_menu(account_no):
    initialize_balance(account_no)

    while True:
        print("\n Welcome to My Bank")
        print("1: Deposit")
        print("2: Withdraw")
        print("3: Balance Check")
        print("4: Exit")
        try:
            choice = int(input("Select option: "))
            match choice:
                case 1:
                    deposit(account_no)
                case 2:
                    withdraw(account_no)
                case 3:
                    balance_check(account_no)
                case 4:
                    print(" Thank you for using our bank!")
                    break
                case _:
                    print(" Invalid option. Choose 1 to 4.")
        except ValueError:
            print(" Please enter a valid number.")


if __name__ == "__main__":
    account = login()
    main_menu(account)
