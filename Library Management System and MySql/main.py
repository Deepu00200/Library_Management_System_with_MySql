from matplotlib import image
import pymysql
from tkinter import *
from PIL import ImageTk,Image #PIL -> Pillow
from tkinter import messagebox
from AddBook import *
from ViewBooks import *
from IssueBook import *
from DeleteBook import *
from ReturnBook import *


con=pymysql.connect(host="localhost", port=3306,user="root",password="123456789",database="libman")

cur=con.cursor() # -> cursor


root=Tk()
root.title("Library")
root.minsize(width=400,height=400)
root.geometry("600x500")


bg = ImageTk.PhotoImage(file="lib.jpg")

canvas =Canvas(root)
canvas.pack(fill=BOTH,expand=True)

canvas.create_image(0,0,image=bg,anchor='nw')

def resize_image(e):
    global image,resized, image2
    image=Image.open("lib.jpg")
    resized=image.resize((e.width,e.height),Image.ANTIALIAS)

    image2=ImageTk.PhotoImage(resized)
    canvas.create_image(0,0,image=image2,anchor='nw')

headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel = Label(headingFrame1, text="Welcome to \n My Library", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(root,text="Add Book Details",bg='black', fg='white', command=addBook)
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
btn2 = Button(root,text="Delete Book",bg='black', fg='white', command=delete)
btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
btn3 = Button(root,text="View Book List",bg='black', fg='white', command=View)
btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
btn4 = Button(root,text="Issue Book to Student",bg='black', fg='white', command = issueBook)
btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)
    
btn5 = Button(root,text="Return Book",bg='black', fg='white', command = returnBook)
btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)
root.mainloop()





root.bind("<Configure>",resize_image)
root.mainloop()
