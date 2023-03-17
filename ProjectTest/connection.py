import psycopg2
#First of all what you have to do
#is run this command in the comandline from windows
# pip install psycopg2-binary 
# This will install the package needed to make a connection (the package that you put at the top of this file)
conn = psycopg2.connect(database="postgres", #This is the name of the database it is by default postgres
                        host="localhost", #This is your computer
                        user="postgres",  #In theory if you didnt change anything this should be your usernam
                        password="jackbali", #Put here your personal password the one from the labs
                        port="5432") #This is your local port jsut leave this number like this

cursor = conn.cursor() #The cursors object is the one that is goijng to help us run things
cursor.execute("SET search_path = 'lab';")  #the execute method will executre your commands
#The search path just makes it so that you can select one of the schemas created I set it here to the one of the lab
cursor.execute("UPDATE artist SET aname ='Charlotte' WHERE aname = 'CharlotteTheSmall'")
# Anything that changes the table requires you to add conn.commit() so that the differences are reflected on the actual database
conn.commit()


print(cursor.fetchall()) #whit this command you can see your commits this is only useful (fpr now) when you execute SELECT queries
conn.close() 

CREATE TABLE Artist(
AName VARCHAR(20),
Birthplace
VARCHAR(20),
Style VARCHAR(20),
DateOfBirth DATE,
PRIMARY KEY(Id));


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