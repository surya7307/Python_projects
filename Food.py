import mysql.connector
import datetime
flag,coffee,tea,cool,hot=0,0,0,0,0
amount=0
username=input("Enter your name or alias name :")
if username=="":
    print("You must enter a name or alias name ")
else:
    while True:
        print("---------PvS Restaurent---------")
        print("1.Order\n2.Pay\n3.Admin\n4.Exit\n")
        ch=int(input("Enter your choice : "))
        if ch==1:
            print("Order.No\t\tFood\t\tPrice")
            print("1\t\tCoffee\t\t20.00\n2\t\tTea\t\t20.00\n3\t\tCool Coffee\t70.00\n4\t\tHot Coffee\t70.00")
            order=int(input("Enter the order number to order your food : "))
            if order==1:
                amount+=20
                coffee+=1
                name="coffee"
            elif order==2:
                amount+=20
                tea+=1
                name="tea"
            elif order==3:
                amount+=70
                cool+=1
                name="cool coffee"
            elif order==4:
                amount+=70
                hot+=1
                name="hot coffee"
            else:
                print("Choose the correct option")
            flag+=2
            con=input("You want to continue  an take order of us ( yes or no ) : ").lower()
            if con=="yes":
                continue
            elif con=="no" :
                mydb=mysql.connector.connect(host="localhost",user="root",password="Samsung753",database="student")
                mycursor=mydb.cursor()
                sql="INSERT INTO food_details(customer_name,order_date,order_time,coffee_qty,tea_qty,coolcoffee_qty,hotcoffee_qty,total_price) Values(%s,%s,%s,%s,%s,%s,%s,%s)"
                var=datetime.datetime.now()
                var_date=var.strftime("%d-%m-%Y")
                var_time=var.strftime("%T")
                val=(username,var_date,var_time,coffee,tea,cool,hot,amount)
                mycursor.execute(sql,val)
                mydb.commit()
            else:
                print("Enter the valid option( yes or no )")
        elif ch==2:
            if flag>2:
                print("Your payment is : ",amount)
            else:
                print("Your payment is 0\nPlease take any order of us")
        elif ch==3:
            password=input("Enter the admin password : ")
            if password=="Samsung753":
                record=input("Enter what records  you want (database(d)) or (current(c)) :").lower()
                if record=="c":
                    print("Customer\t\tCoffee\tTea\tCool Coffee\tHot Coffee\tAmount")
                    print(username,"\t\t",coffee,"\t",tea,"\t",cool,"\t\t",hot,"\t\t",amount)
                    con=input("You want to exit or not (exit or not):").lower()
                    if con=="exit":
                        break
                    elif con=="not":
                        continue
                    else:
                        print("Enter valid option")
                else:
                    mydb=mysql.connector.connect(host="localhost",user="root",password="Samsung753",database="student")
                    mycursor=mydb.cursor()
                    sql2="select * from food_details"
                    mycursor.execute(sql2)
                    result=mycursor.fetchall()
                    for i in result:
                        print(i)
            else:
                print("Enter the correct admin password :(")
        elif ch==4:
            break
        else:
            print("Choose the correct option")
    
