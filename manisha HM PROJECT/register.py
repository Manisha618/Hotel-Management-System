from tkinter import *
from PIL import Image,ImageTk,ImageFilter
from tkinter import messagebox
from tkinter import ttk
import pymysql


class register_page:
    def __init__(self,root):
        self.root =  root
        self.root.title("Register Page")
        self.root.geometry("1400x1000")
        
        # fields of all form entities

        self.var_fname  = StringVar()
        self.var_lname = StringVar()
        self.var_contact_no = StringVar()
        self.var_email = StringVar()
        self.var_password = StringVar()
        self.confirm_password = StringVar()
        self.check_var = BooleanVar()
        

        
        
        # background image  \hotel4.jpeg
        bg_img = Image.open(r"C:\Users\Admin\Desktop\manisha HM PROJECT\image\hotel4.jpeg")
        resize = bg_img.resize((1400,1000)) 
        bgimg = resize.filter(ImageFilter.GaussianBlur(radius=2)) #  img4 = resize.filter(ImageFilter.GaussianBlur(radius=0))
        self.bgimg = ImageTk.PhotoImage(bgimg) 
        image = Label(self.root,image = self.bgimg).place(x=0,y=0) 
        
        # side_bar_image 
        img2  =  Image.open(r"C:\Users\Admin\Desktop\manisha HM PROJECT\image\hotel-management.jpg")
        resize = img2.resize((350,500))
        side_img = resize.filter(ImageFilter.GaussianBlur(radius=0))
        self.side_img = ImageTk.PhotoImage(side_img) 
        image2 = Label(self.root,image = self.side_img).place(x=100,y=70) 
        
        # new frame
        self.frame = Frame(self.root,bg="white",width=550,height=505)
        self.frame.place(x=450,y=70)
        
        # register
        register = Label(self.frame,text="REGISER HERE",font=("times roman",20,"bold"),fg="green",bg="white").place(x=150,y=80)
        
        # first name
        first_name = Label(self.frame,text="First Name",font=("courier",13,"bold"),bg="white",fg="black")
        first_name.place(x=50,y=150)
        first_name_entry = Entry(self.frame,textvariable=self.var_fname).place(x=50,y=175)
        
        #last name
        last_name = Label(self.frame,text="Last Name",font=("courier",13,"bold"),bg="white",fg="black")
        last_name.place(x=300,y=150)
        last_name_entry = Entry(self.frame,textvariable=self.var_lname)
        last_name_entry.place(x=300,y=175)
        
        # contact NO
        contact_no = Label(self.frame,text="Contact No",font=("courier",13,"bold"),bg="white",fg="black")
        contact_no.place(x=50,y=210)
        contact_no_label = Entry(self.frame,textvariable=self.var_contact_no)
        contact_no_label.place(x=50,y=235)
        
        # email
        email= Label(self.frame,text="Email",bg="white",fg="black",font=("courier",13,"bold"))
        email.place(x=300,y=210)
        email_entry= Entry(self.frame,textvariable=self.var_email)
        email_entry.place(x=300,y=235)
        
        #password 
        password = Label(self.frame,text="password",font=("courier",13,"bold"),bg="white",fg="black")
        password.place(x=50,y=270)
        password_entry = Entry(self.frame,textvariable=self.var_password)
        password_entry.place(x=50,y=295)
        
        # confirm password 
        confirm_password = Label(self.frame,text="Confirm password",font=("courier",13,"bold"),bg="white",fg="black")
        confirm_password.place(x=300,y=270)
        confirm_password_entry = Entry(self.frame,textvariabl= self.confirm_password)
        confirm_password_entry.place(x=300,y=295)
        
        # terms and condition 
        check = Checkbutton(self.frame,text="I agree Terms and Condition",variable=self.check_var,font=("courier",10,"bold"),onvalue=1,offvalue=0)
        check.place(x=50,y=350)
        
        # registered img , label and entry 
        
        register_img = Image.open(r"C:\Users\Admin\Desktop\manisha HM PROJECT\image\registerimage.png")
        resize = register_img.resize((150,50))
        img3 = resize.filter(ImageFilter.GaussianBlur(radius=0))
        self.img3 = ImageTk.PhotoImage(img3)
        image = Button(self.frame,image=self.img3,bg="white",command=self.data)
        image.place(x=50,y=400)
        
        # login img , label and entry 
        login_img  = Image.open(r"C:\Users\Admin\Desktop\manisha HM PROJECT\image\loginimage.png")
        resize = login_img.resize((100,40))
        img4 = resize.filter(ImageFilter.GaussianBlur(radius=0))
        self.img4 = ImageTk.PhotoImage(img4)
        image4 = Label(self.frame,image = self.img4,bg="white")
        image4.place(x=200,y=405)
        
       # ----------------------------------   BACKEND WORK ---------------------------------------------------------------
    def data(self):
        if self.var_fname.get() == "" or self.var_lname.get() =="" or self.var_contact_no.get() == "" or self.var_email.get() =="" or self.var_password.get() =="":
            messagebox.showerror("Warning","All fields are required !")
        elif self.var_password.get() != self.confirm_password.get() :
            messagebox.showerror("Warning","Your password does not Match") 
        elif self.check_var.get() == 0:
            messagebox.showerror("Warning","Make sure you agree the terms and conditions")
        else:
            try:
                connect = pymysql.connect(host="localhost",user="root",password="manishasaroj",database="hoteldb") 
                cursor  =  connect.cursor()
                insrtqry = ''' INSERT INTO register(first_name,last_name,contact_no,email,password)
                                  VALUES(%s,%s,%s,%s,%s) '''
                cursor.execute(insrtqry,(self.var_fname.get(),self.var_lname.get(),self.var_contact_no.get(),self.var_email.get(),self.var_password))
                connect.commit()
                cursor.close()
                messagebox.showinfo("Message","Registeration successfull ! ")
                     
                    
                    
            except Exception as e:
                messagebox.showerror("Error",f"Something went wrong:{str(e)}") 
                        
                
        

        
        
        
        
        
        
        
    
    
if __name__ == "__main__":
    root = Tk()
    obj = register_page(root)
    root.mainloop()
    