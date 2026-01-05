import mysql.connector as sqltor1
conn=sqltor1.connect(host="localhost",user="root",password="12345",database="showroom")
mycursor=conn.cursor()
if conn.is_connected():
    print("conection with database established successfully")
else:
    print(" #### connection with database failed ####")

print("****#### WELCOME TO TEJASHVI & ANSH CLOTHES CENTRE ####****")
c1=conn.cursor()
choice=0
while choice != 3 :
    print("1.CREATE YOUR ACCOUNT :-")
    print("2.LOG IN :")
    print("3.EXIT :")
    choice=int(input("ENTER YOUR CHOICE :"))

    if choice== 1:
        cust_name=input("Enter your name:")
        account_no=int(input("Enter your user ID (IN NUMBERS):"))
        password=int(input("Enter your password(IN NUMBERS):"))
        SQL_insert="insert into log_in values ('" +cust_name+"',"+str(account_no)+ ","+str(password)+")"
        c1.execute(SQL_insert)
        conn.commit()
        print("ACCOUNT CREATED")
    if choice ==2:
        print(' ')
        print("--------Enter your Credentials-------")
        cust_name=input("Enter your name:")  
        print(' ')
        account_no=int(input("Enter your user ID (IN NUMBERS):"))
        print(' ')
        password=int(input("Enter your password (IN NUMBERS):"))
        print('')
        c1=conn.cursor()
        c1.execute("select * from log_in")
        data =c1.fetchall()
        count=c1.rowcount
        c2=0
        for row in data:
            if (cust_name in row ) and (account_no in row) and (password in row):
                print(' ')
                print(' ')
                print('****#### WELCOME TO TEJASHVI & ANSH CLOTHES CENTRE ####****')
                print(' ')
                print(' ')
                print('TO SEE COSTUMERS DETAILS,press                                             :1')
                print(' ')
                print('TO KNOW ABOUT THE US,press                                                :2')
                print(' ')
                print('TO SEE  DETAILS OF ALL THE COSTUMERS WHO HAD PAID THE BILL  ,press         :3')
                print(' ')
                print('TO PAY THE BILL,press                                                      :4')
                print(' ')
                print('TO EXIT,press                                                              :5')
                print(' ')
                print('WANT TO RATE US,press                                                      :6')
                print(' ')
                c2=int(input("Enter your choice :"))
                if (c2==1):
                    c1=conn.cursor()
                    c1.execute ('select * from log_in ')
                    data=c1.fetchall()
                    count=c1.rowcount
                    print('details of all employees is :',count)
                    print("details of all employees are  arranged as Name/User ID/passpharse:")
                    for row in data:
                        print(row)
                    conn.commit()
                    print("Visit again")
                elif (c2==2):
                    print("Welcome to TEJASHVI & ANSH CLOTHES CENTRE come today,buy now!!!")
                    print("Get good quality clothes at affordable price")
                    print("All types of clothes are present")
                    print("To know about our terms and conditions visit our website")
                    print("Shop opening and closing times -9:00am-2:00pm and 4:00pm to 9:00pm")
                    print("Contant No.-  9760094215,9669877856")
                    print("Email-tpsansh@gmail.com")
                    print("----thanks for reading----")
                elif(c2==3):
                    c1=conn.cursor()
                    c1.execute('select * from customer_table')
                    data=c1.fetchall()
                    count=c1.rowcount
                    print("Deatils of all Customers is:",count)
                    print("details of all employees are  arranged as Name/price/size/phone no.") 
                    for row in data:
                        print(row)
                    print("------VISIT AGAIN------")
                elif(c2==4):
                    f_name=input("Enter your name :")
                    cloth_code=int(input("Enter cloth code:"))
                    price=int(input("Enter the amount to be paid:"))
                    size=int(input("Enter your customer clothes size :"))
                    phone_no=int(input("Enter customer phone no. :"))
                    SQL_insert="insert into customer_table values ('" +f_name+"',"+str(cloth_code)+","+str(price)+ ","+str(size)+","+str(phone_no)+")"
                    c1.execute(SQL_insert)
                    conn.commit()
                    print("Bill Recorded")
                elif(c2==5):
                    print("-------Thank you For Visiting------")
                elif(c2==6):
                    print("Rate Us For Service")
                    rating=int(input("On the scale of 10 how would you like to rate us:"))
                    if rating >10:
                        print("Thanks for rating beyond limit :-)")
                    else:
                        print("--------Thanks for the rating--------")
                else:
                    print("Oops, something went wrong.....")
                    c1.close
        
    if choice==3:
        print("-----Thanks you for Visiting-----")

