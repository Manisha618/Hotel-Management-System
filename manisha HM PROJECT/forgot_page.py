from tkinter import *
from PIL import Image,ImageTk,ImageFilter

class forgot_password():
    def __init__(self,root):
        self.root = root
        self.root.title("Forgot password")
        self.root.geometry("1400x1000")
        
        # bg image
        bg_image=Image.open(r"C:\Users\Admin\Desktop\manisha HM PROJECT\image\hotel.jpg")
        resize_img = bg_image.resize((1400,900))
        image =  resize_img.filter(ImageFilter.GaussianBlur(radius=0))
        self.imgtk=ImageTk.PhotoImage(image)
        image=Label(root,image=self.imgtk)
        image.place(x=0,y=0,relwidth=1,relheight=1)
        
        # frame
        new_frame = Frame(self.root)
        
        
    
    
if __name__ ==  "__main__":
    root=Tk()
    obj = forgot_password(root)
    root.mainloop()
                