SET search_path = 'lab';
SELECT * from artist


CREATE TABLE hotel_chain(
Id UNIQUE INT,
centAddress VARCHAR,
email VARCHAR,
nTelephone INT,
chainRating INT,
nHotels(),
PRIMARY KEY(Id));

CREATE TABLE hotel{
    hotelAddress VARCHAR,
    Id UNIQUE INT,
    nRooms (),
    nTelephone INT,
    hotel_chain Id,
    hotelRating INT,
}

CREATE TABLE room{
    price FLOAT,
    reference to capcity TABLE,
    eBed BOOLEAN,
    views REFEREENCE TO TABLE views,
    available (),
    rNumber INT,
    ID (rNumber,hID)
}

CREATE TABLE client{
    FirstName         VARCHAR(50) NOT NULL,
    MiddleName    VARCHAR(50),
    LastName          VARCHAR(50)NOT NULL,
    cAddress VARCHAR,
    SSN UNIQUE,
    ID
}

CREATE TABLE employee{
    FirstName         VARCHAR(50) NOT NULL,
    MiddleName    VARCHAR(50),
    LastName          VARCHAR(50)NOT NULL,
    eAddress VARCHAR,
    SSN UNIQUE,
    ID
    role VARCHAR,
}

CREATE TABLE reservation{
    ID
    sTime DATETIME,
    eTime DATETIME,
    c_id FOREIGN KEY,
    h_id FOREIGN KEY,
    views VARCHAR,
    capacity VARCHAR,
    extraBed BOOLEAN
}

CREATE TABLE damage{
    rid FOREIGN KEY,
    description CHAR,
    ID
}

CREATE TABLE commodity{
    ID,
    type CHAR,
    description CHAR
}

CREATE TABLE alloccation_reservation{
    ID, 
    rnumber NOT A FOREIGN KEY INT
    h_id  FOREIGN KEY
}

CREATE TABLE relation{
    AID
    sTime DATETIME,
    eTime DATETIME,
    rNumber INT
}


do you think we should add picture in database for hotels?
 an url or what? I am not sure... 
 ok
