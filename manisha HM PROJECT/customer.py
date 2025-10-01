from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk,ImageFilter
import random
import pymysql
from tkinter import messagebox


class cust_wind:
    def __init__(self,root):
        self.root=root
        self.root.title('CUSTOMER')
        self.root.geometry("1055x440+230+195") # widthxheight+x+y
        
        # -------------------------------- VARIABLES OF DATA 
        
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set((x))
        
        self.var_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_email=StringVar()
        self.var_mobile=StringVar()
        self.var_nationality=StringVar()
        self.var_idproof=StringVar()
        self.var_idnumber=StringVar()
        self.var_address=StringVar()
        
        
        # title 
        title  = Label(self.root,text="Add Customer Details",font=("times roman",17,"bold"),fg ="gold",bg="black")
        title.place(x=0,y=0,width="1055",height="30")
        
        # logo
        img2 = Image.open(r"C:\Users\Admin\Desktop\manisha HM PROJECT\image\hotel_logo.webp")
        img2 =  img2.resize((70,30), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lbl=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lbl.place(x=50,y=0,width=70,height=30)
        
        # customer details
        lblfrm = LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",padx=2,font=("times roman",13,"bold"),fg="black")
        lblfrm.place(x=5,y=30,width=300,height=440)
        
        # custm ref
        lblref = Label(lblfrm,text="Customer Ref :",padx=5,pady=6,font=("arial",10,"bold"))
        lblref.grid(row=0,column=0,sticky=W)
        entry_ref =ttk.Entry(lblfrm,width="21",textvariable=self.var_ref,font=("times roman",10,"bold"),state="readonly")
        entry_ref.grid(row=0,column=1)
        
        #cust name
        cname = Label(lblfrm,text="Customer Name : ",padx=5,pady=6,font=("arial",10,"bold"))
        cname.grid(row=1,column=0,sticky=W)
        c_n =ttk.Entry(lblfrm,width="21",textvariable=self.var_name,font=("times roman",10,"bold"))
        c_n.grid(row=1,column=1)
        
        #mother name
        mname = Label(lblfrm,text="Mother Name : ",padx=5,pady=6,font=("arial",10,"bold"))
        mname.grid(row=2,column=0,sticky=W)
        m_e =ttk.Entry(lblfrm,width="21",textvariable=self.var_mother,font=("times roman",10,"bold"))
        m_e.grid(row=2,column=1)
        
        # gender
        gen = Label(lblfrm,text="Gender :  ",padx=5,pady=6,font=("arial",10,"bold"))
        gen.grid(row=3,column=0,sticky=W)
        gen_e =ttk.Combobox(lblfrm,textvariable=self.var_gender,font=("times roman",10,"bold"),width=20)
        gen_e['values'] = ("Male","Female","Other")
        gen_e.current(0)
        gen_e.grid(row=3,column=1)
        
        #post code
        pcode = Label(lblfrm,text="Post code:  ",padx=5,pady=6,font=("arial",10,"bold"))
        pcode.grid(row=4,column=0,sticky=W)
        p_e =ttk.Entry(lblfrm,width="21",textvariable=self.var_post,font=("times roman",10,"bold"))
        p_e.grid(row=4,column=1)
        
        # mobile bo.
        mno = Label(lblfrm,text="Email ",padx=5,pady=6,font=("arial",10,"bold"))
        mno.grid(row=5,column=0,sticky=W)
        mno_e =ttk.Entry(lblfrm,width="21",textvariable=self.var_mobile,font=("times roman",10,"bold"))
        mno_e.grid(row=5,column=1)
        
        # email
        mail = Label(lblfrm,text="Mobile Number: ",padx=5,pady=6,font=("arial",10,"bold"))
        mail.grid(row=6,column=0,sticky=W)
        mail_e =ttk.Entry(lblfrm,width="21",textvariable=self.var_email,font=("times roman",10,"bold"))
        mail_e.grid(row=6,column=1)
        
        #Nationality
        nation = Label(lblfrm,text="Nationality : ",padx=5,pady=6,font=("arial",10,"bold"))
        nation.grid(row=7,column=0,sticky=W)
        nation_e =ttk.Combobox(lblfrm,width="21",textvariable=self.var_nationality,font=("times roman",10,"bold"))
        nation_e['values'] = ("Indian","Brazillian","American","others")
        nation_e.current(0)
        nation_e.grid(row=7,column=1)
        
        # idproof
        id = Label(lblfrm,text=" Id : ",padx=5,pady=6,font=("arial",10,"bold"))
        id .grid(row=8,column=0,sticky=W)
        id_e =ttk.Combobox(lblfrm,textvariable=self.var_idproof,font=("times roman",10,"bold"),width=20)
        id_e['values'] = ("Adharcard","pen card","other")
        id_e.current(0)
        id_e.grid(row=8,column=1)
        
        #id no.
        idno = Label(lblfrm,text="Id Number: ",padx=5,pady=6,font=("arial",10,"bold"))
        idno.grid(row=9,column=0,sticky=W)
        idno_e =ttk.Entry(lblfrm,width="21",textvariable=self.var_idnumber,font=("times roman",10,"bold"))
        idno_e.grid(row=9,column=1)
        
        # address
        add = Label(lblfrm,text="Address : ",padx=5,pady=6,font=("arial",10,"bold"))
        add.grid(row=10,column=0,sticky=W)
        add_e =ttk.Entry(lblfrm,width=21,textvariable=self.var_address,font=("times roman",10,"bold"))
        add_e.grid(row=10,column=1)
        
        # btns 
        btnadd=Button(lblfrm,text="Add",command=self.addbtn,font=("times roman",10,"bold"),width=5,bg="black",fg="gold")
        btnadd.place(x=5,y=355)
        btnup=Button(lblfrm,text="Update",command=self.update,font=("times roman",10,"bold"),width=7,bg="black",fg="gold")
        btnup.place(x=65,y=355)
        btnadd=Button(lblfrm,text="Delete",command=self.delete,font=("times roman",10,"bold"),width=7,bg="black",fg="gold")
        btnadd.place(x=140,y=355)
        btnadd=Button(lblfrm,text="Reset",command=self.reset,font=("times roman",10,"bold"),width=7,bg="black",fg="gold")
        btnadd.place(x=217,y=355)
        
        
        #-----  view details and search system 
        lblfrm2=LabelFrame(self.root,text="View Customer Details & Search ",font=("times roman","10","bold"))
        lblfrm2.place(x=320,y=30,width="715",height="400")
        
        # search by
        
        lbl = Label(lblfrm2,text="Search By",font=("times roman","12","bold"),fg="white",bg="red")
        lbl.place(x=2,y=2,width="90",height="30") 
        # select option
        self.search_column = StringVar()
        sltbox= ttk.Combobox(lblfrm2,text="Select Option ",textvariable=self.search_column,font=("times roman",10,"bold"))
        sltbox['values'] = ("ref","email")
        sltbox.current(0)
        sltbox.place(x=110,y=2,width="120",height="27")
        
        self.search_value  = StringVar()
        sltbox_e = Entry(lblfrm2,textvariable=self.search_value,font=("times roman","12","bold"))
        sltbox_e.place(x=240,y=2,width="120",height="27")
        # search btn
        searchbtn = Button(lblfrm2,text="SEARCH",command=self.search_ref,font=("times roman","12","bold"),fg="white",bg="green")
        searchbtn.place(x=370,y=2,width="120",height="27")
        # show all btn
        searchall = Button(lblfrm2,text="SHOW All",command=self.fetch_data,font=("times roman","12","bold"),fg="white",bg="green")
        searchall.place(x=500,y=2,width="120",height="27")
        
        #------------------------------- SHOW DATA TABLE --------------------------
        
        detail_table = Frame(lblfrm2,bd=2,relief="ridge")
        detail_table.place(x=5,y=40,width="700",height="300")
        
         # scroll bar 
        scroll_x = ttk.Scrollbar(detail_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(detail_table,orient=VERTICAL)
        
        # make a table 
        self.cust_detail_table = ttk.Treeview(detail_table,column=("ref","Name","Mother","Gender","Post","Mobile",
                                              "email","nationality","idproof","idnumber","address",),
                                              xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y) 
        
        
        
        
        scroll_x.config(command=self.cust_detail_table.xview)
        scroll_y.config(command=self.cust_detail_table.yview)
        
        # to show the column heading with referece value 
        self.cust_detail_table.heading("ref",text="Refer No")
        self.cust_detail_table.heading("Name",text="Name")
        self.cust_detail_table.heading("Mother",text="Mother Name")
        self.cust_detail_table.heading("Gender",text="Gender")
        self.cust_detail_table.heading("Post",text="Post")
        self.cust_detail_table.heading("Mobile",text="Mobile No")
        self.cust_detail_table.heading("email",text="Email")
        self.cust_detail_table.heading("nationality",text="Nationality")
        self.cust_detail_table.heading("idproof",text="Id Proof")
        self.cust_detail_table.heading("idnumber",text="Id Number")
        self.cust_detail_table.heading("address",text="Address")
        
        self.cust_detail_table["show"]="headings"
        
        # column ka width kam krne ke liye 
        self.cust_detail_table.column("ref",width=100)
        self.cust_detail_table.column("Name",width=100)
        self.cust_detail_table.column("Mother",width=100)
        self.cust_detail_table.column("Gender",width=100)
        self.cust_detail_table.column("Post",width=100)
        self.cust_detail_table.column("Mobile",width=100)
        self.cust_detail_table.column("email",width=100)
        self.cust_detail_table.column("nationality",width=100)
        self.cust_detail_table.column("idproof",width=100)
        self.cust_detail_table.column("idnumber",width=100)
        self.cust_detail_table.column("address",width=100)
        
        self.cust_detail_table.pack(fill=BOTH,expand=1)
        
        #widget.bind("<Event>", function_reference)
        #- widget: The GUI element (like a button, label, or table).
        #"<Event>": A string that describes the user action.
        # function_reference: The function that should run when the event happens.
        self.cust_detail_table.bind("<ButtonRelease-1>",self.get_cursor)
        #buttonRelease-1 means Left mouse button release (it's a mouse action )
        self.fetch_data()
        
    # add  bnt functionality 
        
    def addbtn(self):
        if self.var_name.get()=="" or self.var_mother.get()=="" or self.var_gender.get()=="" or self.var_post.get()=="" or self.var_email.get=="" or self.var_mobile.get()=="" or self.var_nationality.get()=="" or self.var_idnumber.get()=="" or self.var_address.get()=="":
            messagebox.showerror('Error',"All fields are Required",parent=self.root) # parent (msg self.root me hi show hoga not on others root )
        else:
            try:
                conn = pymysql.connect(host="localhost",user="root",password="manishasaroj",database="hoteldb") 
                cursor  =  conn.cursor()
                
                insertqry = ''' INSERT INTO customer(ref,
                                                    Name,
                                                    Mother,
                                                    Gender,
                                                    Post,
                                                    Mobile,
                                                    email,
                                                    nationality,
                                                    idproof,
                                                    idnumber,
                                                    address)
                                    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
                cursor.execute(insertqry,(self.var_ref.get(),self.var_name.get(),self.var_mother.get(),self.var_gender.get(),self.var_post.get(),self.var_email.get(),self.var_mobile.get(),
                                          self.var_nationality.get(),self.var_idproof.get(),self.var_idnumber.get(),self.var_address.get()))
                conn.commit()
                self.fetch_data() # add hone ke baad , data call hoga
                conn.close()
                messagebox.showinfo('Message',"Your data is added ",parent=self.root)
        
            except Exception as  e:
                messagebox.showerror("Error",f"something went wrong {e}",parent=self.root)
                
    def fetch_data(self):
        try:
            conn = pymysql.connect(host="localhost",user="root",password="manishasaroj",database="hoteldb")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from customer")
            rows = my_cursor.fetchall() 
            if len(rows) !=0:
                self.cust_detail_table.delete(*self.cust_detail_table.get_children())
                for i in rows:
                    self.cust_detail_table.insert("",END,values=i)
            conn.commit()
            conn.close()
        except Exception as  e:
                messagebox.showerror("Error",f"{e}",parent=self.root)
                
    # ------------ view details and search system  me jo data show ho rha hai , uspe clicke  krne pe , customer details pe return show hone lge , or update bhi kr sake  
    def get_cursor(self,event=""):
        cursor_row = self.cust_detail_table.focus()
        # focus()is called without arguments to get the selected item.
        content = self.cust_detail_table.item(cursor_row) 
         # Retrieves the full content (dictionary) of the selected row.
        row = content["values"]
        #Extracts just the list of values from the selected row  These are the actual data entries (e.g., name, email, mobile, etc.)          
        if row and len(row) >= 11: # it means row ke andar 11 values honi chahiye use jada nahi
            self.var_ref.set(row[0]),  
            self.var_name.set(row[1]), 
            self.var_mother.set(row[2]), 
            self.var_gender.set(row[3]),  
            self.var_post.set(row[4]),  
            self.var_email.set(row[5]), 
            self.var_mobile.set(row[6]), 
            self.var_nationality.set(row[7]), 
            self.var_idproof.set(row[8]), 
            self.var_idnumber.set(row[9]), 
            self.var_address.set(row[10])
        # These variables are likely linked to entry widgets or labels in the GUI.
        # So when a row is selected, the form fields get auto-filled with that row’s data
        else:
            print("no row selected")
            
            
       # update btn     
    def update(self):
        if self.var_mobile.get() == "":
            messagebox.showError("Error","please enter the number ")
        else:
            conn=pymysql.connect(host="localhost",user="root",password="manishasaroj",database="hoteldb")
            mycursor=conn.cursor()
            query= """UPDATE customer SET Name=%s,Mother=%s,Gender=%s,Post=%s,Mobile=%s,email=%s,nationality=%s,idproof=%s,idnumber=%s,address=%s where ref=%s """
            values=(self.var_name.get(),self.var_mother.get(),self.var_gender.get(),self.var_post.get(),self.var_mobile.get(),self.var_email.get(),self.var_nationality.get(),self.var_idproof.get(),self.var_idnumber.get(),self.var_address.get(),self.var_ref.get())
            mycursor.execute(query,values)
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo('Message',"your data updated",parent=self.root)
    
    def delete(self):
        ans = messagebox.askyesno("Hotel Management System","Do You Want to Delete this Customer",parent=self.root)
        if ans>0:
            conn = pymysql.connect(host="localhost",user="root",password="manishasaroj",database="hoteldb")
            my_cursor=conn.cursor()
            qury = """ delete from customer where ref = %s """ 
            values = (self.var_ref.get())
            my_cursor.execute(qury,values)
        else:
            if not ans:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
                       
    def reset(self):
        x=random.randint(1000,9999)
        self.var_ref.set((x))
        #self.var_ref=StringVar()
        
        #self.var_ref.set(""),  
        self.var_name.set(""), 
        self.var_mother.set(""), 
        #self.var_gender.set(""),  
        self.var_post.set(""),  
        self.var_email.set(""), 
        self.var_mobile.set(""), 
        #self.var_nationality.set(""), 
        #self.var_idproof.set(""), 
        self.var_idnumber.set(""), 
        self.var_address.set("")
    
    def search_ref(self):
            conn=pymysql.connect(host="localhost",user="root",password="manishasaroj",database="hoteldb")
            my_cursor=conn.cursor()
            qry  = f" select * from customer where {self.search_column.get()} LIKE %s"
            value = f"%{self.search_value.get()}%"
            my_cursor.execute(qry,value)
            rows=my_cursor.fetchall()
            if rows:
                self.cust_detail_table.delete(*self.cust_detail_table.get_children())
                for row in rows:
                    self.cust_detail_table.insert("","end",values=row)
            conn.commit()  
            conn.close()
        
            #messagebox.showerror("error","no such referce found")
            
    
        
        
        
        
            
                
        
if __name__ == "__main__":
    root = Tk()
    obj = cust_wind(root)
    root.mainloop()  