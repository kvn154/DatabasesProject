SET search_path = 'SAILORS';
CREATE TABLE payment(
    payment_ID int NOT NULL,
    amount FLOAT,
    method VARCHAR(25),
    client_ID int NOT NULL,
    FOREIGN KEY (client_ID) REFERENCES client,
    location_ID int NOT NULL,
    FOREIGN KEY (location_ID) REFERENCES location,
    PRIMARY KEY(payment_ID)
);