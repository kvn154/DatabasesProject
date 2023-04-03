import psycopg2
#First of all what you have to do
#is run this command in the comandline from windows
# pip install psycopg2-binary 
# This will install the package needed to make a connection (the package that you put at the top of this file)
conn = psycopg2.connect(database='postgres', #This is the name of the database it is by default postgres
                        host='localhost', #This is your computer
                        user='postgres',  #In theory if you didnt change anything this should be your usernam
                        password='jackbali', #Put here your personal password the one from the labs
                        port='5432') #This is your local port jsut leave this number like this

cursor = conn.cursor() #The cursors object is the one that is goijng to help us run things
cursor.execute('SET search_path = 'lab';')  #the execute method will executre your commands
#The search path just makes it so that you can select one of the schemas created I set it here to the one of the lab
cursor.execute('UPDATE artist SET aname ='Charlotte' WHERE aname = 'CharlotteTheSmall'')
# Anything that changes the table requires you to add conn.commit() so that the differences are reflected on the actual database
conn.commit()


print(cursor.fetchall()) #whit this command you can see your commits this is only useful (fpr now) when you execute SELECT queries
conn.close() 
