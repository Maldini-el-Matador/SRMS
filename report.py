from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3

class reportclass:
	def __init__(self,root):
			self.root= root
			self.root.title("Student Result Management System")
			self.root.geometry("1200x480+80+170")
			self.root.config(bg="white")
			self.root.focus_force()

			title = Label(self.root,text = "view student results",font=("goudy old style", 20),fg="#262626" , bg= "orange").place(x= 10, y=15, width=1180, height=50)

			self.var_search = StringVar()

			lbl_search= Label(self.root, text ="Search by roll number", font =("goudy old style", 20,"bold"),bg= "white").place(x= 270, y=100)
			txt_search= Entry(self.root, textvariable =self.var_search, font =("goudy old style", 20,),bg= "lightyellow").place(x= 520, y=100, width = 150)	

			self.btn_search = Button(self.root, text ="Search",font= ("goudy old style", 15,"bold"),bg ="#0319f4", fg="White", cursor ="hand2",command =None)
			self.btn_search.place(x= 680, y=100, width =100, height = 28)

			self.btn_clear = Button(self.root, text ="Clear",font= ("goudy old style", 15,"bold"),bg ="Gray", fg="White", cursor ="hand2",command =None)
			self.btn_clear.place(x= 800, y=100, width =100, height = 28)

			lbl_roll= Label(self.root, text ="select student", font =("goudy old style", 20,"bold"),bg= "white").place(x= 50, y=100)
			lbl_name= Label(self.root, text ="name", font =("goudy old style", 20,"bold"),bg= "white").place(x= 50, y=160)
			lbl_course= Label(self.root, text ="course", font =("goudy old style", 20,"bold"),bg= "white").place(x= 50, y=220)
			lbl_marks= Label(self.root, text ="marks obtained", font =("goudy old style", 20,"bold"),bg= "white").place(x= 50, y=280)
			lbl_full= Label(self.root, text ="full marks", font =("goudy old style", 20,"bold"),bg= "white").place(x= 50, y=340)
			lbl_per= Label(self.root, text ="full marks", font =("goudy old style", 20,"bold"),bg= "white").place(x= 50, y=340)


if __name__ == "__main__":
	root = Tk()
	obj = reportclass(root)
	root.mainloop()			