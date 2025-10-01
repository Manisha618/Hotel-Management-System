from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk,ImageFilter
import random
from time import strftime
from datetime import datetime
import pymysql
from tkinter import messagebox
from PIL import Image,ImageTk,ImageFilter


class room_booking_wind: 
    def __init__(self,root):
        self.root=root
        self.root.title('CUSTOMER')
        self.root.geometry("1055x440+230+195") # widthxheight+x+y
        
        # title 
        title  = Label(self.root,text="ROOM BOOKING",font=("times roman",17,"bold"),fg ="gold",bg="black")
        title.place(x=0,y=0,width="1055",height="30")
        
        # logo
        img2 = Image.open(r"C:\Users\Admin\Desktop\manisha HM PROJECT\image\hotel_logo.webp")
        img2 =  img2.resize((70,30), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lbl=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lbl.place(x=50,y=0,width=70,height=30)
        
        # customer details
        lblfrm = LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",padx=2,font=("times roman",13,"bold"),fg="black")
        lblfrm.place(x=5,y=30,width=330,height=410)
        
        # variable 
        
        self.var_contact=StringVar()
        self.var_check_in_date=StringVar()
        self.var_check_out_date=StringVar()
        self.var_room_type=StringVar()
        self.var_available_rooms=StringVar()
        self.var_meals=StringVar() 
        self.var_no_of_days=StringVar()
        self.var_paid_tax=StringVar()
        self.var_actual_total=StringVar()
        self.var_total_cost=StringVar() 
        
        
        # custm phone no
        cust_phone_no = Label(lblfrm,text="Customer Phone No :",padx=5,pady=6,font=("arial",10,"bold"))
        cust_phone_no.grid(row=0,column=0,sticky=W)
        cust_phone_no_e=ttk.Entry(lblfrm,textvariable=self.var_contact,width="15",font=("times roman",10,"bold"))
        cust_phone_no_e.place(x=150,y=2,width="110",height="25")
        
        # fetch btn
        fetch=Button(lblfrm,text="Fetch",command=self.fetch_data,font=("times roman","10","bold"),fg="gold",bg="black",width="2")
        fetch.place(x=265,y=3,width="55",height="25")
        
        #check in Date
        check_in_date = Label(lblfrm,text="Check-in-Date : ",padx=5,pady=6,font=("arial",10,"bold"))
        check_in_date.grid(row=1,column=0,sticky=W)
        check_in_date_e=ttk.Entry(lblfrm,textvariable=self.var_check_in_date,width="21",font=("times roman",10,"bold"))
        check_in_date_e.grid(row=1,column=1)
        
        #check out date
        check_out_date = Label(lblfrm,text="Check-out-Date: ",padx=5,pady=6,font=("arial",10,"bold"))
        check_out_date.grid(row=2,column=0,sticky=W)
        check_out_date_e=ttk.Entry(lblfrm,textvariable=self.var_check_out_date,width="21",font=("times roman",10,"bold"))
        check_out_date_e.grid(row=2,column=1)
        
        # Room Type
        room_type = Label(lblfrm,text="Room Type:  ",padx=5,pady=6,font=("arial",10,"bold"))
        room_type.grid(row=3,column=0,sticky=W)
        room_type_e =ttk.Combobox(lblfrm,textvariable=self.var_room_type,font=("times roman",10,"bold"),width=20)
        room_type_e['values'] = ("single","Double","Luxury")
        room_type_e.current(0)
        room_type_e.grid(row=3,column=1)
        
        # available rooms
        ava_rooms = Label(lblfrm,text="Available Room:",padx=5,pady=6,font=("arial",10,"bold"))
        ava_rooms.grid(row=4,column=0,sticky=W)
        conn = pymysql.connect(host="localhost",user="root",password="manishasaroj",database="hoteldb")
        my_cursor=conn.cursor()
        my_cursor.execute("select room_no from room_details")
        rows = my_cursor.fetchall() 
        ava_rooms =ttk.Combobox(lblfrm,textvariable=self.var_available_rooms,width="21",font=("times roman",10,"bold"))
        ava_rooms["values"]=rows
        ava_rooms.current(0)
        ava_rooms.grid(row=4,column=1)
        
        # Meal
        meal = Label(lblfrm,text="Meal :",padx=5,pady=6,font=("arial",10,"bold"))
        meal.grid(row=5,column=0,sticky=W)
        meal =ttk.Combobox(lblfrm,textvariable=self.var_meals,width="21",font=("times roman",10,"bold"))
        meal["values"]=("Breakfast","Lunch","Dinner")
        meal.current(0)
        meal.grid(row=5,column=1)
        
        # No. of days
        no_of_days = Label(lblfrm,text="No. of Days: ",padx=5,pady=6,font=("arial",10,"bold"))
        no_of_days.grid(row=6,column=0,sticky=W)
        no_of_days =ttk.Entry(lblfrm,textvariable=self.var_no_of_days,width="21",font=("times roman",10,"bold"))
        no_of_days.grid(row=6,column=1)
        
        #paid Tax 
        tax = Label(lblfrm,text="Paid Tax: ",padx=5,pady=6,font=("arial",10,"bold"))
        tax.grid(row=7,column=0,sticky=W)
        tax =ttk.Entry(lblfrm,textvariable=self.var_paid_tax,width="21",font=("times roman",10,"bold"))
        tax.grid(row=7,column=1)
        
        # Actual total
        total = Label(lblfrm,text="Least Price : ",padx=5,pady=6,font=("arial",10,"bold"))
        total.grid(row=8,column=0,sticky=W)
        total=ttk.Combobox(lblfrm,textvariable=self.var_actual_total,font=("times roman",10,"bold"),width=20)
        total.grid(row=8,column=1)
        
        #total cost
        total_cost = Label(lblfrm,text="Total Cost: ",padx=5,pady=6,font=("arial",10,"bold"))
        total_cost.grid(row=9,column=0,sticky=W)
        total_cost=ttk.Entry(lblfrm,textvariable=self.var_total_cost,width="21",font=("times roman",10,"bold"))
        total_cost.grid(row=9,column=1)
        
        # btns
        bill= Button(lblfrm,text="Bill: ",command=self.total,font=("times roman",10,"bold"),width=10,bg="black",fg="gold")
        bill.place(x=4,y=320) 
        
        Add=Button(lblfrm,text="Add",command=self.add,font=("times roman",10,"bold"),width=5,bg="black",fg="gold")
        Add.place(x=5,y=355)
        
        update=Button(lblfrm,text="Update",command=self.update,font=("times roman",10,"bold"),width=7,bg="black",fg="gold")
        update.place(x=65,y=355)
        
        delete=Button(lblfrm,text="Delete",command=self.delete,font=("times roman",10,"bold"),width=7,bg="black",fg="gold")
        delete.place(x=140,y=355)
        
        reset=Button(lblfrm,text="Reset",command=self.reset,font=("times roman",10,"bold"),width=7,bg="black",fg="gold")
        reset.place(x=217,y=355)
        
        #-----  view details and search system 
        lblfrm2=LabelFrame(self.root,text="View Customer Details & Search ",font=("times roman","10","bold"))
        lblfrm2.place(x=340,y=240,width="695",height="200")
        # search by
        lbl = Label(lblfrm2,text="Search By",font=("times roman","12","bold"),fg="white",bg="red")
        lbl.place(x=2,y=2,width="90",height="30") 
        # select option
        self.search_column = StringVar()
        sltbox= ttk.Combobox(lblfrm2,text="Select Option ",textvariable=self.search_column,font=("times roman",10,"bold"))
        sltbox['values'] = ("Mobile","available_rooms")
        sltbox.current(0)
        sltbox.place(x=110,y=2,width="120",height="27")
        
        self.search_value  = StringVar()
        sltbox_e = Entry(lblfrm2,textvariable=self.search_value,font=("times roman","12","bold"))
        sltbox_e.place(x=240,y=2,width="120",height="27")
        
        # search btn
        searchbtn = Button(lblfrm2,text="SEARCH",command=self.search_system,font=("times roman","12","bold"),fg="white",bg="green")
        searchbtn.place(x=370,y=2,width="120",height="27")
        
        # show all data
        searchall = Button(lblfrm2,text="SHOW All",command=self.fetch_data_room,font=("times roman","12","bold"),fg="white",bg="green")
        searchall.place(x=500,y=2,width="120",height="27")
        
        # right side image
        img = Image.open(r"C:\Users\Admin\Desktop\manisha HM PROJECT\image\room.jpg")
        img = img.resize((400, 210), Image.Resampling.LANCZOS)  # Use Resampling for Pillow >=10
        # Convert to Tkinter-compatible image-
        self.photoimg1 = ImageTk.PhotoImage(img)
        # Display image in label
        lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=630, y=30, width=400, height=210)
        
        #------------------------------- SHOW DATA TABLE --------------------------
        detail_table = Frame(lblfrm2,bd=2,relief="ridge")
        detail_table.place(x=5,y=40,width="690",height="130")
        
         # scroll bar 
        scroll_x = ttk.Scrollbar(detail_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(detail_table,orient=VERTICAL)
        
        # make a table 
        self.room_book = ttk.Treeview(detail_table,column=("mobile","checkin","checkout","roomtype","roomavailable","meal",
                                              "noOfdays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.room_book.xview)
        scroll_y.config(command=self.room_book.yview)
        
        # to show the column heading with referece value 
        self.room_book.heading("mobile",text="Contact")
        self.room_book.heading("checkin",text="check-in")
        self.room_book.heading("checkout",text="check-out")
        self.room_book.heading("roomtype",text="Room Type")
        self.room_book.heading("roomavailable",text="Available Rooms") 
        self.room_book.heading("meal",text="Meal")
        self.room_book.heading("noOfdays",text="No of Days")
        self.room_book["show"]="headings"
        
        # column ka width kam krne ke liye 
        self.room_book.column("mobile",width=100)
        self.room_book.column("checkin",width=100)
        self.room_book.column("checkout",width=100)
        self.room_book.column("roomtype",width=100)
        self.room_book.column("roomavailable",width=100)
        self.room_book.column("meal",width=100)
        self.room_book.column("noOfdays",width=100)
        self.room_book.pack(fill=BOTH,expand=1)
        self.fetch_data_room()
        self.room_book.bind("<ButtonRelease-1>",self.get_cursor)
        
        
        
        
 # ------------------------------------------- add btn -------------------------------------------
 
        
        
    def add(self):
        if self.var_contact.get()=="" or  self.var_check_in_date.get()=="" or self.var_check_out_date.get()=="" or self.var_room_type.get()=="" or self.var_available_rooms.get()=="" or self.var_meals.get()=="" or  self.var_no_of_days.get()=="" :
            raise messagebox.showerror("Error","All fields required",parent=self.root)
        else:
            conn =  pymysql.connect(host="localhost",user="root",password="manishasaroj",database="hoteldb")
            my_cursor=conn.cursor() 
            query = ''' insert into room (Mobile,
                                        check_in_date,
                                        check_out,
                                        room_type,
                                        available_rooms,
                                        meal,
                                        no_of_days
                                        )
                    VALUES(%s,%s,%s,%s,%s,%s,%s) ''' 
            my_cursor.execute(query,(self.var_contact.get(),
                                     self.var_check_in_date.get(),
                                     self.var_check_out_date.get(),
                                     self.var_room_type.get(),
                                     self.var_available_rooms.get(),
                                     self.var_meals.get(),
                                     self.var_no_of_days.get()
                                     ))
            messagebox.showinfo("Message","your data is added ",parent=self.root)
            conn.commit()
            self.fetch_data_room()
            conn.close()
    
    # row table  , ke data ko fetch kia gya hia
    def fetch_data_room(self):
        try:
            conn = pymysql.connect(host="localhost",user="root",password="manishasaroj",database="hoteldb")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from room")
            rows = my_cursor.fetchall() 
            if len(rows) !=0:
                self.room_book.delete(*self.room_book.get_children())
                for i in rows:
                    self.room_book.insert("",END,values=i)
            conn.commit()
            conn.close()
        except Exception as  e:
                messagebox.showerror("Error",f"{e}",parent=self.root)
                
                
    # jo row pe select kre , us row ka data , left hand side ke field me show ho jaye
    def get_cursor(self,event=""):
        cursor_row = self.room_book.focus()
        # focus()is called without arguments to get the selected item.
        content = self.room_book.item(cursor_row) 
         # Retrieves the full content (dictionary) of the selected row.
        row = content["values"]
        #Extracts just the list of values from the selected row  These are the actual data entries (e.g., name, email, mobile, etc.)          
        if row and len(row) >= 6: # it means row ke andar 11 values honi chahiye use jada nahi
            self.var_contact.set(row[0]),
            self.var_check_in_date.set(row[1]),
            self.var_check_out_date.set(row[2]),
            self.var_room_type.set(row[3]),
            self.var_available_rooms.set(row[4]),
            self.var_meals.set(row[5]),
            self.var_no_of_days.set(row[6])
        # These variables are likely linked to entry widgets or labels in the GUI.
        # So when a row is selected, the form fields get auto-filled with that row’s data
        else:
            print("no row selected")
       
        
 #------------------------- fetch all data like name , gender , nationality , address ------------------ 
    
    def fetch_data(self):
        contact = self.var_contact.get().strip()
        if contact == "":
            messagebox.showerror("Error", "Enter The Number", parent=self.root)
            return
        try:
            conn = pymysql.connect(host="localhost", user="root", password="manishasaroj", database="hoteldb")
            mycursor = conn.cursor()
            query = "SELECT Name, Gender, Address, Nationality FROM customer WHERE Mobile=%s"
            value = (contact,)
            mycursor.execute(query, value)
            row = mycursor.fetchone() 
            conn.close()

            if row is None:
                messagebox.showerror("Error", "This data not found", parent=self.root)
                return

            showdataframe = Frame(self.root, bd=2, relief=RIDGE)
            showdataframe.place(x=350, y=40, width=260, height=150)

            # Name
            lblname = Label(showdataframe, text="Name: ", font=("arial", 10, "bold"))
            lblname.place(x=0, y=10)
            lblname_e = Entry(showdataframe, font=("arial", 10, "bold"))
            lblname_e.insert(0, row[0])
            lblname_e.place(x=80, y=10)

            # Gender
            lblgender = Label(showdataframe, text="Gender: ", font=("arial", 10, "bold"))
            lblgender.place(x=0, y=40)
            lblgender_e = Entry(showdataframe, font=("arial", 10, "bold"))
            lblgender_e.insert(0, row[1])
            lblgender_e.place(x=80, y=40)

            # Address
            lbladd = Label(showdataframe, text="Address: ", font=("arial", 10, "bold"))
            lbladd.place(x=0, y=70)
            lbladd_e = Entry(showdataframe, font=("arial", 10, "bold"))
            lbladd_e.insert(0, row[2])
            lbladd_e.place(x=80, y=70)

            # Nationality
            lblnation = Label(showdataframe, text="Nationality: ", font=("arial", 10, "bold"))
            lblnation.place(x=0, y=100)
            lblnation_e = Entry(showdataframe, font=("arial", 10, "bold"))
            lblnation_e.insert(0, row[3])
            lblnation_e.place(x=80, y=100)

        except Exception as e:
            messagebox.showerror("Error", f"Database error: {str(e)}", parent=self.root)
            
    # update btn
    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter the  Contact field")
        else:
            conn=pymysql.connect(host="localhost",user="root",password="manishasaroj",database="hoteldb")
            my_cursor=conn.cursor()
            #query=""" update room set check_in_date=%s,check_out=%s,room_type=%s,available_rooms=%s,meal=%s,no_of_days=%s WHERE Mobile=%s """
            #values=(self.var_check_in_date.get(),self.var_check_out_date.get(),self.var_room_type.get(),self.var_available_rooms.get(),self.var_meals.get(),self.var_no_of_days.get(),self.var_contact.get())
            my_cursor.execute("update room set check_in_date=%s,check_out=%s,room_type=%s,meal=%s,no_of_days=%s WHERE available_rooms=%s",(self.var_check_in_date.get(),
                                                                                                                                                     self.var_check_out_date.get(),
                                                                                                                                                     self.var_room_type.get(),
                                                                                                                                                    self.var_meals.get(),
                                                                                                                                                     self.var_no_of_days.get(),
                                                                                                                                                     self.var_available_rooms.get()
                                                                                                                                                     )
                              )
            conn.commit()
            conn.close()
            messagebox.showinfo("Message","your customer  data  has been  updated",parent=self.root)
            
    def delete(self):
        ans =  messagebox.askyesno("Hotel Managemeny System","Do you want to delete this customer",parent=self.root)
        if ans>0:
            conn=pymysql.connect(host="localhost",user="root",password="manishasaroj",database="hoteldb")
            mycursor=conn.cursor()
            mycursor.execute("delete from room where available_rooms=%s",(self.var_available_rooms.get()))
            messagebox.showinfo("Message","your customer rooms data has been deleted",parent=self.root)
        else:
            if not ans:
                return 
        conn.commit()
        self.fetch_data()
        conn.close()
        
    def reset(self):
        self.var_contact.set(""),
        self.var_check_in_date.set(""),
        self.var_check_out_date.set(""),
        self.var_room_type.set(""),
        self.var_meals.set(""),
        self.var_no_of_days.set(""),
        self.var_available_rooms.set("")
        self.var_paid_tax.set("")
        self.var_actual_total.set("")
        self.var_total_cost.set("")
        
    def total(self):
        check_in_date=self.var_check_in_date.get()
        check_out_date=self.var_check_out_date.get()
        check_in_date=datetime.strptime(check_in_date,"%d/%m/%Y")
        check_out_date=datetime.strptime(check_out_date,"%d/%m/%Y")
        self.var_no_of_days.set(abs(check_out_date-check_in_date).days)
        no_of_days = int(self.var_no_of_days.get())
        print("total function executed")
        
        if (self.var_meals.get().strip() in ["Breakfast","Lunch","Dinner"] and self.var_room_type.get().strip() == "Luxury"):
            print("if block wala statement")
            meal_rate = 300.0 
            room_rate = 900.0 
            daily_base_rate = meal_rate + room_rate
            base_cost = no_of_days * daily_base_rate 
            tax_value = base_cost * 0.10  # 10% tax 

            # Format values for display
            tax_amount = "Rs. " + "%.2f" % tax_value
            sub_total = "Rs. " + "%.2f" % base_cost
            actual_total = "Rs. " + "%.2f" % (base_cost + tax_value)
            
            print(tax_amount)
            print(sub_total)
            print(actual_total)

            # Update GUI variables
            self.var_paid_tax.set(tax_amount)
            self.var_actual_total.set(sub_total)
            self.var_total_cost.set(actual_total)
            
        elif (self.var_meals.get().strip() in ["Breakfast","Lunch","Dinner"] and self.var_room_type.get().strip() == "Double"):
            print("if block wala statement")
            meal_rate = 200.0 
            room_rate = 600.0 
            daily_base_rate = meal_rate + room_rate
            base_cost = no_of_days * daily_base_rate 
            tax_value = base_cost * 0.10  # 10% tax 

            # Format values for display
            tax_amount = "Rs. " + "%.2f" % tax_value
            sub_total = "Rs. " + "%.2f" % base_cost
            actual_total = "Rs. " + "%.2f" % (base_cost + tax_value)
            
            print(tax_amount)
            print(sub_total)
            print(actual_total)

            # Update GUI variables
            self.var_paid_tax.set(tax_amount)
            self.var_actual_total.set(sub_total)
            self.var_total_cost.set(actual_total)
            
        elif (self.var_meals.get().strip() in ["Breakfast","Lunch","Dinner"] and self.var_room_type.get().strip() == "Single"):
            print("if block wala statement")
            meal_rate = 100.0 
            room_rate = 300.0 
            daily_base_rate = meal_rate + room_rate
            base_cost = no_of_days * daily_base_rate 
            tax_value = base_cost * 0.10  # 10% tax 

            # Format values for display
            tax_amount = "Rs. " + "%.2f" % tax_value
            sub_total = "Rs. " + "%.2f" % base_cost
            actual_total = "Rs. " + "%.2f" % (base_cost + tax_value)
            
            print(tax_amount)
            print(sub_total)
            print(actual_total)

            # Update GUI variables
            self.var_paid_tax.set(tax_amount)
            self.var_actual_total.set(sub_total)
            self.var_total_cost.set(actual_total)
            
        else:
            messagebox.showerror("Messge","Invalid meal or room type selected",parent=self.root)
                
    def search_system(self):
         conn = pymysql.connect(host="localhost",user="root",password="manishasaroj",database="hoteldb")
         my_cursor=conn.cursor()
         query = f"select * from room where {self.search_column.get() } Like %s"
         value = f"%{self.search_value.get()}%"
         my_cursor.execute(query,value)
         rows = my_cursor.fetchall()
         if rows:
                self.room_book.delete(*self.room_book.get_children())
                for row in rows:
                    self.room_book.insert("","end",values=row)
                    
    
if __name__ == "__main__":
    root = Tk()
    obj = room_booking_wind(root)
    root.mainloop()  
    