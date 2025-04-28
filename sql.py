import mysql.connector as a

con=a.connect(host="localhost",user="root",password="Tritiya12345@",database="university")
def ast():
    
    a=input("enter the roll no of the student::")

    b=input("enter the name of the student::")

    z=input("enter the semester::")

    d=input("enter the section of the student::")

    e=input("enter the address of the student::")

    f=input("enter the phoneno of the student::")

    data=(a,b,z,d,e,f)

    sql='insert into student values(%s,%s,%s,%s,%s,%s)'

    c=con.cursor()

    c.execute(sql,data)

    con.commit()

    print("data entered successfully")

    print(">---------------------------------------------------------------------------------------------------------<")

def dsec():

    cl=input("enter the section to get student list:::")

    data=(cl,)

    sql="select*from student where section =%s"

    c=con.cursor()

    c.execute(sql,data)

    d=c.fetchall()

    for i in d:

        print("rollno:",i[0])

        print("name:",i[1])

        print("semester:",i[2])

        print("section:",i[3])

        print("address:",i[4])

        print("phoneno:",i[5])

        print(">----------------------------------------------------<")

    print("data shown successfully")

    print(">---------------------------------------------------------------------------------------------------------<")
 