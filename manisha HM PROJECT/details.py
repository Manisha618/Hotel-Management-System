from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
from PIL import Image,ImageTk,ImageFilter



class details_window:
    def __init__(self,root):
        self.root = root 
        self.root.title("Detail Page")
        self.root.geometry("1055x440+230+195")
        
        #title
        lbl=Label(self.root,text="Room Adding Department",font=("Arial","20","bold"),fg="yellow",bg="black")
        lbl.place(x=0,y=0,width="1055",height="30")
        
        # logo
        img2 = Image.open(r"C:\Users\Admin\Desktop\manisha HM PROJECT\image\hotel_logo.webp")
        img2 =  img2.resize((70,30), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lbl=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lbl.place(x=50,y=0,width=70,height=30)
        
        # Frame 
        frm = LabelFrame(self.root,bd=2,relief=RIDGE,text="New Rooms Details",padx=2,font=("arial","10","bold"))
        frm.place(x=5,y=50,width=450,height=300)
        
        # images
        img3 = Image.open(r"C:\Users\Admin\Desktop\manisha HM PROJECT\image\room.jpg")
        img3 =  img3.resize((150,70), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lbl=Label(frm,image=self.photoimg3,bd=0,relief=RIDGE)
        lbl.place(x=2,y=1,width=150,height=70)
        
        img4 = Image.open(r"C:\Users\Admin\Desktop\manisha HM PROJECT\image\swimmingpool.jpg")
        img4 =  img4.resize((150,70), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        lbl=Label(frm,image=self.photoimg4,bd=0,relief=RIDGE)
        lbl.place(x=160,y=1,width=150,height=70) 
        
        img5 = Image.open(r"C:\Users\Admin\Desktop\manisha HM PROJECT\image\loby.jpg")
        img5 =  img5.resize((120,70), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        lbl=Label(frm,image=self.photoimg5,bd=0,relief=RIDGE)
        lbl.place(x=320,y=1,width=120,height=70)
        
        
        
        # variables 
        self.var_floor = StringVar()
        self.var_room_no = StringVar()
        self.var_room_type = StringVar() 
        
        
        # entry fields
        
        floor = Label(frm,text="Floor",font=("Times roman","10","bold"))
        floor.place(x=20,y=100)
        entry_floor = Entry(frm,textvariable=self.var_floor,font=("arial","10","bold"))
        entry_floor.place(x=120,y=100)
        
        room_no = Label(frm,text="Room NO",font=("Times roman","10","bold"))
        room_no.place(x=20,y=130)
        room_entry  =Entry(frm,textvariable=self.var_room_no,font=("Times roman","10","bold"))
        room_entry.place(x=120,y=130)
        
        room_type = Label(frm,text="Room Type",font=("times roman","10","bold"))
        room_type.place(x=20,y=160)
        
        room_type_entry=ttk.Combobox(frm,textvariable=self.var_room_type,font=("times roman","10","bold"))
        room_type_entry['values']=("select option","Single","Double","Luxury")
        room_type_entry.current(0)
        room_type_entry.place(x=120,y=160)
        
        # buttons 
        add = Button(frm,text="Add",command=self.add,font=("arial","10","bold"),fg="yellow",bg="black",bd="1")
        add.place(x=2,y=210,width="60",height="30")
        
        update = Button(frm,command=self.update,text="Update",font=("arial","10","bold"),fg="yellow",bg="black",bd="1")
        update.place(x=70,y=210,width="60",height="30")
        
        dlt = Button(frm,command=self.delete,text="Delete",font=("arial","10","bold"),fg="yellow",bg="black",bd="1")
        dlt.place(x=140,y=210,width="60",height="30")
        
        clear = Button(frm,command=self.reset,text="Reset",font=("arial","10","bold"),fg="yellow",bg="black",bd="1")
        clear.place(x=210,y=210,width="60",height="30")
        
         
        
        # show room details table
        detail_table = Frame(self.root,bd=2,relief="ridge")
        detail_table.place(x=500,y=50,width="500",height="300")
        
         # scroll bar 
        scroll_x = ttk.Scrollbar(detail_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(detail_table,orient=VERTICAL)
        
        # make a table 
        self.cust_detail_table = ttk.Treeview(detail_table,column=("floor","room_no","room_type"),
                                              xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y) 
        
        
        
        
        scroll_x.config(command=self.cust_detail_table.xview)
        scroll_y.config(command=self.cust_detail_table.yview)
        
        # to show the column heading with referece value 
        self.cust_detail_table.heading("floor",text="Floor")
        self.cust_detail_table.heading("room_no",text="Room No")
        self.cust_detail_table.heading("room_type",text="Room Type")
        
        
        self.cust_detail_table["show"]="headings"
        
        # column ka width kam krne ke liye 
        self.cust_detail_table.column("floor",width=100)
        self.cust_detail_table.column("room_no",width=100)
        self.cust_detail_table.column("room_type",width=100)
        
        
        self.cust_detail_table.pack(fill=BOTH,expand=1)
        self.cust_detail_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
 # add btn functionality 
    def add(self):
            if self.var_floor.get()=="" or self.var_room_no.get()=="" or self.var_room_type.get()=="" :
                messagebox.showerror("error","please entry the all fields")
            conn = pymysql.connect(host="localhost",user="root",password="manishasaroj",database="hoteldb")
            my_cursor=conn.cursor()
            query = """ insert into room_details(floor,room_no,room_type) values(%s,%s,%s)"""
            my_cursor.execute(query,(self.var_floor.get(),self.var_room_no.get(),self.var_room_type.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("message","your data has been added")  
            
    def fetch_data(self):
        try:
            conn = pymysql.connect(host="localhost",user="root",password="manishasaroj",database="hoteldb")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from room_details")
            rows = my_cursor.fetchall() 
            if len(rows) !=0:
                self.cust_detail_table.delete(*self.cust_detail_table.get_children())
                for i in rows:
                    self.cust_detail_table.insert("",END,values=i)
            conn.commit()
            conn.close()
        except Exception as  e:
                messagebox.showerror("Error",f"{e}",parent=self.root)
                
    def get_cursor(self,event=""):
        cursor_row = self.cust_detail_table.focus()
        # focus()is called without arguments to get the selected item.
        content = self.cust_detail_table.item(cursor_row) 
         # Retrieves the full content (dictionary) of the selected row.
        row = content["values"]
        #Extracts just the list of values from the selected row  These are the actual data entries (e.g., name, email, mobile, etc.)          
        if row and len(row) >= 2: # it means row ke andar 11 values honi chahiye use jada nahi
            self.var_floor.set(row[0]),  
            self.var_room_no.set(row[1]), 
            self.var_room_type.set(row[2])
           
        # These variables are likely linked to entry widgets or labels in the GUI.
        # So when a row is selected, the form fields get auto-filled with that row’s data
        else:
            print("no row selected")
                
                
    def update(self):
        if self.var_floor.get()=="":
            messagebox.showerror("error","please enter all  the fields")
        conn = pymysql.connect(host="localhost",user="root",password="manishasaroj",database="hoteldb")
        my_cursor=conn.cursor()
        query = """ update room_details set floor=%s, room_type=%s where room_no = %s"""
        my_cursor.execute(query,(self.var_floor.get(),self.var_room_type.get(),self.var_room_no.get()))
        conn.commit()
        conn.close()
        messagebox.showinfo("messag","your data has been updated")
        
    def delete(self):
        ans = messagebox.askyesno("Hotel Management System","Do You Want to Delete this Customer",parent=self.root)
        if ans>0:
            conn = pymysql.connect(host="localhost",user="root",password="manishasaroj",database="hoteldb")
            my_cursor=conn.cursor()
            query = """ delete  from room_details where room_no=%s"""
            my_cursor.execute(query,(self.var_room_no.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo("message","your data has been deleted",parent= self.root)
            
    def reset(self):
        self.var_floor.set(""),  
        self.var_room_no.set(""), 
        self.var_room_type.set("")
        
            

        
                
       
        
        
        
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    root =Tk()
    obj=details_window(root)
    root.mainloop()
        
        
        