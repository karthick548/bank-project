CREATE DATABASE user_db;

USE user_db;

CREATE TABLE user_details (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    father_name VARCHAR(50),
    phone VARCHAR(15),
    house_no VARCHAR(50),
    street VARCHAR(100),
    landmark VARCHAR(100),
    city VARCHAR(50),
    state VARCHAR(50),
    pincode VARCHAR(10),
    dob DATE,
    aadhaar VARCHAR(20) NOT NULL UNIQUE,
    pan VARCHAR(15) NOT NULL UNIQUE,
    account_no VARCHAR(20) NOT NULL UNIQUE
);

--------------------------------------
USE user_db;

CREATE TABLE IF NOT EXISTS account_credentials (
    id INT AUTO_INCREMENT PRIMARY KEY,
    account_no VARCHAR(20) UNIQUE NOT NULL,
    pin VARCHAR(4) NOT NULL,
    FOREIGN KEY (account_no) REFERENCES user_details(account_no)
);

--------------------------------
CREATE TABLE IF NOT EXISTS account_balance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    account_no VARCHAR(20) UNIQUE,
    balance DOUBLE DEFAULT 0,
    FOREIGN KEY (account_no) REFERENCES user_details(account_no)
);
