from tkinter import *
from PIL import Image,ImageTk,ImageFilter
from register import register_page
from tkinter import messagebox
from tkinter import ttk
import pymysql
from Home_page import HOME_PAGE 


# function to open regiter page
def open_register():
    new_win = Toplevel(root)
    new_win.reg_page = register_page(new_win)

class login_window:
    def __init__(self,root):
        self.root = root
        self.root.title("Login page")
        self.root.geometry("1500x1000")
        
        header = Label(root,text="HOTEL MANAGEMENT SYSTEM",bg="black",fg="yellow",font=("Arial",25,"bold"),width="100")
        header.place(x=0,y=0)
         # C:\Users\Admin\Desktop\manisha HM PROJECT\image
                
        bg_image=Image.open(r"C:\Users\Admin\Desktop\manisha HM PROJECT\image\hotel.jpg")
        resize_img = bg_image.resize((1400,900))
        image =  resize_img.filter(ImageFilter.GaussianBlur(radius=0))
        self.imgtk=ImageTk.PhotoImage(image)
        image=Label(root,image=self.imgtk)
        image.place(x=0,y=0,relwidth=1,relheight=1)
        
        self.frame = Frame(root,bg="black",bd=40)
        self.frame.place(x=450,y=100,height="450",width="370")
        
        # image2 (usericon on login page)
        user_icon = Image.open(r"C:\Users\Admin\Desktop\manisha HM PROJECT\image\changebg.png")
        resize = user_icon.resize((100,100))
        image2 = resize.filter(ImageFilter.GaussianBlur(radius=0))
        self.img2=ImageTk.PhotoImage(image2)
        image2 = Label(self.frame,image=self.img2,bd=0,bg="red")
        image2.place(x=100,y=-50)
        msg = Label(self.frame,text="Get Started",font=("Arial",20,"bold"),bg="black",fg="white").place(x=80,y=40)
        
        # fields
        self.var_user_name=StringVar()
        self.var_password=StringVar()
        
        
        # user name 
        username=Image.open(r"C:\Users\Admin\Desktop\manisha HM PROJECT\image\changebg.png")
        resize2 = username.resize((40,40))
        image3 = resize2.filter(ImageFilter.GaussianBlur(radius=0))
        self.image3 = ImageTk.PhotoImage(image3)
        image3 = Label(self.frame,image=self.image3,bd=0,bg="red")
        image3.place(x=10,y=100)
        user_name_label = Label(self.frame,font=("Arial",10,"bold"),fg="white",bg="black",text="User Name").place(x=60,y=110)
        user_name_entry = Entry(self.frame,textvariable=self.var_user_name,width="47",bd="1",fg="black").place(x=20,y=135)
        
        password_img = Image.open(r"C:\Users\Admin\Desktop\manisha HM PROJECT\image\password-removebg-preview.png")
        resize = password_img.resize((40,40))
        img4 = resize.filter(ImageFilter.GaussianBlur(radius=0))
        self.img4 = ImageTk.PhotoImage(img4)
        image4 = Label(self.frame,image=self.img4,bd=0,bg="white").place(x=10,y=170)
        password_label = Label(self.frame,text="Password",bg="black",fg="white",font=("Arial",10,"bold")).place(x=60,y=180)
        password_entry = Entry(self.frame,textvariable=self.var_password,bd=1,bg="white",fg="black",width="47").place(x=20,y=210)
        
        # login button
        login_btn = Button(self.frame,command=self.login,text="Login",bg="red",fg="white",width="10",height="1",bd="0",font=("Courier",15,"bold"))
        login_btn.place(x=80,y=270)
        
        # New user register btn
        new_user_register = Button(self.frame,text="New User Register",bg="black",fg="white",bd="0",font=("courier",10,"bold"),command=open_register)
        new_user_register.place(x=20,y=320)
        
            
        # Forgot password btn
        forgot_password = Button(self.frame,text="Forgot Password",bg="black",fg="white",bd="0",font=("courier",10,"bold"))
        forgot_password.place(x=20,y=343)
        
        # self.var_user_name=StringVar()
        # self.var_password
        
    def login(self):
        if self.var_user_name.get()=="" or self.var_password.get()=="" :
            messagebox.showerror("error","All Fields are required",parent=self.root)
        elif self.var_user_name.get()=='?' and  self.var_password.get()=='?' :
            messagebox.showinfo("welcome to our hotel ")
        else :
            conn=pymysql.connect(host="localhost",user="root",password="manishasaroj",database="hoteldb")
            cursor=conn.cursor()
            cursor.execute("select * from register where first_name=%s and password=%s",(self.var_user_name.get(),self.var_password.get()))
            row=cursor.fetchone()
            conn.close()
            
            if row is None:
                messagebox.showwarning("error","Invalid username or password")
            else:
                access=messagebox.askyesno("Message","Access only admin",parent=self.root)
                if access:
                    self.Hotel_window=Toplevel(self.root) 
                    self.obj=HOME_PAGE(self.Hotel_window)

    
    
        
        
        
        
        
        
        
    
    


if __name__ == "__main__":
    root = Tk()
    obj = login_window(root)
    root.mainloop()