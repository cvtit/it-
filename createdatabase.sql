CREATE DATABASE railwaydata;

USE railwaydata;

CREATE TABLE passenger (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    total INT,
    date DATE
);

CREATE TABLE train (
    train_id INT AUTO_INCREMENT PRIMARY KEY,
    train_name VARCHAR(100),
    boogie_type VARCHAR(20),
    seats_available INT
);

CREATE TABLE reservation (
    pnr_no INT AUTO_INCREMENT PRIMARY KEY,
    passenger_id INT,
    train_id INT,
    seats INT,
    status VARCHAR(20),
    FOREIGN KEY (passenger_id) REFERENCES passenger(id),
    FOREIGN KEY (train_id) REFERENCES train(train_id)
);
