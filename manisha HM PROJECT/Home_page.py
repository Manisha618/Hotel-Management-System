from tkinter import *
from PIL import Image,ImageTk,ImageFilter
from customer import cust_wind
from booking_room import room_booking_wind 
from details import details_window


class HOME_PAGE: 
    def __init__(self,root):
        self.root = root
        self.root.title("WECOME TO HOME PAGE")
        self.root.geometry("1400x1000")
        
        # ----------------------- set the upper image
        img1 = Image.open(r"C:\Users\Admin\Desktop\manisha HM PROJECT\image\shravanihotel.jpg")
        img1 = img1.resize((1550, 140), Image.Resampling.LANCZOS)  # Use Resampling for Pillow >=10
        # Convert to Tkinter-compatible image-
        self.photoimg1 = ImageTk.PhotoImage(img1)
        # Display image in label
        lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1550, height=140)
        
        #------------------- logo image----------------
        img2 = Image.open(r"C:\Users\Admin\Desktop\manisha HM PROJECT\image\hotel_logo.webp")
        img2 =  img2.resize((200,140), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lbl=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lbl.place(x=0,y=0,width=200,height=140)

        
        #--------------- title  --------------------
        lbl=Label(self.root,text="HOTEL MANGEMENT SYSTEM",font=("times roman",20,"bold"),fg="gold",bg="black",bd=4,relief=RIDGE)
        lbl.place(x=0,y=120,width="1400",height="50")
        
        # MAIN FRAME
        main_frame = Frame(self.root,bd=4,relief='ridge')
        main_frame.place(x=0,y=160,width="1400",height="810")
        #  MENU
        lbl = Label(main_frame,text="Menu",bg="black",fg="gold",font=('times roman',20,"bold"),bd=1,relief=RIDGE)
        lbl.place(x=0,y=0,width="230")
        # BTN FRAME
        btn_frame = Frame(main_frame,bd=4,relief='ridge')
        btn_frame.place(x=0,y=35,width="228",height="190")
        
        # btns are here
        btn = Button(btn_frame,text="CUSTOMER",command=self.custumer_page,width="22",bg="black",fg="gold",font=("times roman",14,"bold"),bd=0,relief=RIDGE,cursor="hand1")
        btn.grid(row=0,column=0,pady=1)
        
        btn = Button(btn_frame,text="Room",command=self.room_book_page , width="22",bg="black",fg="gold",font=("times roman",14,"bold"),bd=0,relief=RIDGE,cursor="hand1")
        btn.grid(row=1,column=0,pady=1)
        
        btn = Button(btn_frame,text="DETAILS",command=self.detail_page,width="22",bg="black",fg="gold",font=("times roman",14,"bold"),bd=0,relief=RIDGE,cursor="hand1")
        btn.grid(row=2,column=0,pady=1)
        
        btn = Button(btn_frame,text="REPORT",width="22",bg="black",fg="gold",font=("times roman",14,"bold"),bd=0,relief=RIDGE,cursor="hand1")
        btn.grid(row=3,column=0,pady=1)
        
        btn = Button(btn_frame,text="LOGOUT",width="22",bg="black",fg="gold",font=("times roman",14,"bold"),bd=0,relief=RIDGE,cursor="hand1")
        btn.grid(row=4,column=0,pady=1)
       
       # ----------------------- right side image ----
        img3 = Image.open(r"C:\Users\Admin\Desktop\manisha HM PROJECT\image\andara-resort-and-villas.jpg")
        img3 =  img3.resize((1310,590), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3) 
        lbl=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lbl.place(x=225,y=0,width=1310,height=590) 
        
        img4 = Image.open(r"C:\Users\Admin\Desktop\manisha HM PROJECT\image\food.jpeg")
        img4 =  img4.resize((225,150), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4) 
        lbl=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lbl.place(x=0,y=225,width=225,height=150) 
        
        img5 = Image.open(r"C:\Users\Admin\Desktop\manisha HM PROJECT\image\home_page_main_img.jpg")
        img5 =  img5.resize((225,200), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5) 
        lbl=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lbl.place(x=0,y=350,width=225,height=200)
        
    def custumer_page(self):
        self.new_window = Toplevel(self.root)
        self.customer_class  = cust_wind(self.new_window)
        
    def room_book_page(self):
        self.new_window2 = Toplevel(self.root)
        self.room_booking_class  = room_booking_wind(self.new_window2)
        
    def detail_page(self):
        self.new_window3 = Toplevel(self.root)
        self.details_class  =details_window(self.new_window3)
        
        
        
    
    
    
    
    
    
    
if __name__ == "__main__":
    root = Tk()
    obj = HOME_PAGE(root)
    root.mainloop()
    
    
    
