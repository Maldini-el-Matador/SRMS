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

			self.var_id= ""

			lbl_search= Label(self.root, text ="Search by roll number", font =("goudy old style", 20,"bold"),bg= "white").place(x= 270, y=100)
			txt_search= Entry(self.root, textvariable =self.var_search, font =("goudy old style", 20,),bg= "lightyellow").place(x= 520, y=100, width = 150)	

			self.btn_search = Button(self.root, text ="Search",font= ("goudy old style", 15,"bold"),bg ="#0319f4", fg="White", cursor ="hand2",command =self.search)
			self.btn_search.place(x= 680, y=100, width =100, height = 28)

			self.btn_clear = Button(self.root, text ="Clear",font= ("goudy old style", 15,"bold"),bg ="Gray", fg="White", cursor ="hand2",command =self.clear)
			self.btn_clear.place(x= 800, y=100, width =100, height = 28)

			lbl_roll= Label(self.root, text ="select student", font =("goudy old style", 15,"bold"),relief = GROOVE,bg= "white").place(x= 150, y=230,width = 150, height= 50)
			lbl_name= Label(self.root, text ="name", font =("goudy old style", 15,"bold"),relief = GROOVE,bg= "white").place(x= 300, y=230,width = 150,height= 50)
			lbl_course= Label(self.root, text ="course", font =("goudy old style", 15,"bold"),relief = GROOVE,bg= "white").place(x= 450, y=230,width = 150,height= 50)
			lbl_marks= Label(self.root, text ="marks obtained", font =("goudy old style", 15,"bold"),relief = GROOVE,bg= "white").place(x= 600, y=230,width = 150,height= 50)
			lbl_full= Label(self.root, text ="full marks", font =("goudy old style", 15,"bold"),relief = GROOVE,bg= "white").place(x= 750, y=230,width = 150,height= 50)
			lbl_per= Label(self.root, text ="full marks", font =("goudy old style", 15,"bold"),relief = GROOVE,bg= "white").place(x= 900, y=230,width = 150,height= 50)

			self.roll= Label(self.root, font =("goudy old style", 15,"bold"),relief = GROOVE,bg= "white")
			self.roll.place(x= 150, y=280,width = 150, height= 50)
			self.name= Label(self.root, font =("goudy old style", 15,"bold"),relief = GROOVE,bg= "white")
			self.name.place(x= 300, y=280,width = 150,height= 50)
			self.course= Label(self.root, font =("goudy old style", 15,"bold"),relief = GROOVE,bg= "white")
			self.course.place(x= 450, y=280,width = 150,height= 50)
			self.marks= Label(self.root, font =("goudy old style", 15,"bold"),relief = GROOVE,bg= "white")
			self.marks.place(x= 600, y=280,width = 150,height= 50)
			self.full= Label(self.root, font =("goudy old style", 15,"bold"),relief = GROOVE,bg= "white")
			self.full.place(x= 750, y=280,width = 150,height= 50)
			self.per= Label(self.root, font =("goudy old style", 15,"bold"),relief = GROOVE,bg= "white")
			self.per.place(x= 900, y=280,width = 150,height= 50)

			self.btn_delete = Button(self.root, text ="Delete",font= ("goudy old style", 15,"bold"),bg ="Red", fg="White", cursor ="hand2",command =self.delete)
			self.btn_delete.place(x= 500, y=350, width =150, height = 28)

	def search(self):
		con = sqlite3.connect(database= "rms.db")
		cur = con.cursor()

		try:
			if self.var_search.get()=="":
				messagebox.showerror("Error","roll no is required", parent = self.root)
			else:
				cur.execute("select * from result where roll=?", (self.var_search.get(),))
				row= cur.fetchone()
				if row != None:
					self.var_id= row[0]
					self.roll.config(text=row[1])
					self.name.config(text=row[2])
					self.course.config(text=row[3])
					self.marks.config(text=row[4])
					self.full.config(text=row[5])
					self.per.config(text=row[6])
					

				else:
					messagebox.showerror("Error","no record found", parent =self.root)
		except Exception as ex:
			messagebox.showerror("Error", f"Error due to {str(ex)}")

	def clear(self):
		self.var_id= ""
		self.roll.config(text="")
		self.name.config(text="")
		self.course.config(text="")
		self.marks.config(text="")
		self.full.config(text="")
		self.per.config(text="")
		self.var_search.set("")

	def delete(self):
		con = sqlite3.connect(database= "rms.db")
		cur = con.cursor()

		try:
			if self.var_id== "":
				messagebox.showerror("Error", "student name is required", parent= self.root)
			else:
				cur.execute("select * from result where rid=?",(self.var_id,))
				row = cur.fetchone()
				if row == None:
					messagebox.showerror("Error", "invalid student result", parent= self.root)
				else:
					op=messagebox.askyesno("confirm","do you really want to delete?", parent = self.root)
					if op == True:
						cur.execute("delete from result where rid=?", (self.var_id,))
						con.commit()
						messagebox.showinfo("deleted", "result deleted", parent = self.root)
						self.clear()
		except Exception as ex:
			messagebox.showerror("Error", f"Error due to {str(ex)}")

if __name__ == "__main__":
	root = Tk()
	obj = reportclass(root)
	root.mainloop()			