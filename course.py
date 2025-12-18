from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3

class courseclass:
	def __init__(self,root):
			self.root= root
			self.root.title("Student Result Management System")
			self.root.geometry("1200x480+80+170")
			self.root.config(bg="white")
			self.root.focus_force()

			title = Label(self.root,text = "course details manage",font=("goudy old style", 20),fg="white" , bg= "#033054").place(x= 10, y=15, width=1180, height=35)

			self.var_coursename = StringVar()
			self.var_duration= StringVar()
			self.var_charges= StringVar()
			self.var_description = StringVar()
			self.var_search = StringVar()

			lbl_coursename = Label(self.root,text = "Course Name",font=("goudy old style", 15,"bold"),bg="white").place(x= 10, y=60)
			lbl_duration= Label(self.root,text = "Duration",font=("goudy old style", 15,"bold"),bg="white").place(x= 10, y=100)
			lbl_charges = Label(self.root,text = "Charges",font=("goudy old style", 15,"bold"),bg="white").place(x= 10, y=140)
			lbl_description=Label(self.root,text = "Description",font=("goudy old style", 15,"bold"),bg="white").place(x= 10, y=180)

			self.txt_coursename=Entry(self.root,textvariable= self.var_coursename,font=("goudy old style", 15,"bold"),bg="lightyellow")
			self.txt_coursename.place(x= 150, y=60, width = 200)
			txt_duration=Entry(self.root,textvariable = self.var_duration,font=("goudy old style", 15,"bold"), bg= "lightyellow").place(x= 150, y=100, width=200)
			txt_charges=Entry(self.root,textvariable = self.var_charges,font=("goudy old style", 15,"bold"), bg= "lightyellow").place(x= 150, y= 140,width=200)
			self.txt_description=Text(self.root,font=("goudy old style", 15,"bold"),bg="lightyellow")
			self.txt_description.place(x= 150, y=180, width= 500, height = 100)


			self.btn_add = Button(self.root, text ="Save",font= ("goudy old style", 15,"bold"),bg ="#2196f3", fg="White", cursor ="hand2", command= self.add)
			self.btn_add.place(x= 150, y=400, width =110, height = 40)
			self.btn_update = Button(self.root, text ="Update",font= ("goudy old style", 15,"bold"),bg ="#4caf50", fg="White", cursor ="hand2",command = self.update)
			self.btn_update.place(x= 270, y=400, width =110, height = 40)
			self.btn_delete = Button(self.root, text ="Delete",font= ("goudy old style", 15,"bold"),bg ="#f44336", fg="White", cursor ="hand2",command = self.delete)
			self.btn_delete.place(x= 390, y=400, width =110, height = 40)
			self.btn_clear = Button(self.root, text ="Clear",font= ("goudy old style", 15,"bold"),bg ="#607d8b", fg="White", cursor ="hand2",command =self.clear)
			self.btn_clear.place(x= 510, y=400, width =110, height = 40)

			lbl_search_coursename = Label(self.root, text="course name", font= ("goudy old style", 15,"bold"),bg="White").place(x=720, y=60)
			lbl_search_coursename = Entry(self.root, textvariable = self.var_search, font= ("goudy old style", 15,"bold"),bg="lightyellow").place(x=870, y=60, width= 180)

			self.btn_search = Button(self.root, text ="Search",font= ("goudy old style", 15,"bold"),bg ="#0319f4", fg="White", cursor ="hand2",command =self.search)
			self.btn_search.place(x= 1070, y=60, width =120, height = 28)


			self.c_frame= Frame(self.root, bd = 2 , relief = RIDGE)
			self.c_frame.place(x= 720,y=100, width =470, height = 340)

			scrolly = Scrollbar(self.c_frame,orient = VERTICAL)
			scrollx = Scrollbar(self.c_frame,orient = HORIZONTAL)

			self.coursetable = ttk.Treeview(self.c_frame,columns = ("cid", "name", "duration", "charges", "description"), xscrollcommand = scrollx.set, yscrollcommand= scrolly.set)

			scrollx.pack(side= BOTTOM, fill= X)
			scrolly.pack(side= RIGHT, fill= Y)

			scrollx.config(command= self.coursetable.xview)
			scrolly.config(command= self.coursetable.yview)

			self.coursetable.heading("cid",text ="Course ID")
			self.coursetable.heading("name",text ="Course name")
			self.coursetable.heading("duration",text ="Duration")
			self.coursetable.heading("charges",text ="Charges")
			self.coursetable.heading("description",text ="Description")
			self.coursetable.pack(fill=BOTH, expand= 1)
			self.coursetable["show"] = 'headings'
			self.coursetable.column("cid", width = 50)
			self.coursetable.column("name",width =100 )
			self.coursetable.column("duration",width =100 )
			self.coursetable.column("charges",width = 100)
			self.coursetable.column("description",width =150 )
			self.coursetable.pack(fill=BOTH, expand= 1)
			self.coursetable.bind("<ButtonRelease-1>",self.get_data)
			self.show()

	def clear(self):
		self.show()
		self.var_coursename.set("")
		self.var_duration.set("")
		self.var_search.set("")
		self.var_charges.set("")
		self.txt_description.delete('1.0', END)
		self.txt_coursename.config(state='normal')

	def delete(self):
		con = sqlite3.connect(database= "rms.db")
		cur = con.cursor()

		try:
			if self.var_coursename.get() == "":
				messagebox.showerror("Error", "course name is required", parent= self.root)
			else:
				cur.execute("select * from course where name=?",(self.var_coursename.get(),))
				row = cur.fetchone()
				if row == None:
					messagebox.showerror("Error", "select course from the list first", parent= self.root)
				else:
					op=messagebox.askyesno("confirm","do you really want to delete?", parent = self.root)
					if op == True:
						cur.execute("delete from course where name=?", (self.var_coursename.get(),))
						con.commit()
						messagebox.showinfo("deleted", "course deleted", parent = self.root)
						self.clear()
		except Exception as ex:
			messagebox.showerror("Error", f"Error due to {str(ex)}")

	def get_data(self,ev):
		self.txt_coursename.config(state='readonly')
		r=self.coursetable.focus()
		content= self.coursetable.item(r)
		row= content["values"]
		self.var_coursename.set(row[1])
		self.var_duration.set(row[2])
		self.var_charges.set(row[3])
		self.txt_description.delete('1.0', END)
		self.txt_description.insert(END,row[4])


	def add(self):
		con = sqlite3.connect(database= "rms.db")
		cur = con.cursor()

		try:
			if self.var_coursename.get() == "":
				messagebox.showerror("Error", "course name is required", parent= self.root)
			else:
				cur.execute("select * from course where name=?",(self.var_coursename.get(),))
				row = cur.fetchone()
				if row != None:
					messagebox.showerror("Error", "course name already present", parent= self.root)
				else:
					cur.execute("insert into course(name,duration,charges,description) values(?,?,?,?)",(
						self.var_coursename.get(),
						self.var_duration.get(),
						self.var_charges.get(),
						self.txt_description.get("1.0",END)
						))
					con.commit()
					messagebox.showinfo("Success", "Course added successfully",parent = self.root)
					self.show()

		except Exception as ex:
			messagebox.showerror("Error", f"Error due to {str(ex)}")

	def update(self):
		con = sqlite3.connect(database= "rms.db")
		cur = con.cursor()

		try:
			if self.var_coursename.get() == "":
				messagebox.showerror("Error", "course name is required", parent= self.root)
			else:
				cur.execute("select * from course where name=?",(self.var_coursename.get(),))
				row = cur.fetchone()
				if row == None:
					messagebox.showerror("Error", "select course from list", parent= self.root)
				else:
					cur.execute("update  course set duration=?,charges=?,description=? where name=?",(
						self.var_duration.get(),
						self.var_charges.get(),
						self.txt_description.get("1.0",END),
						self.var_coursename.get()
						))
					con.commit()
					messagebox.showinfo("Success", "Course updated successfully",parent = self.root)
					self.show()

		except Exception as ex:
			messagebox.showerror("Error", f"Error due to {str(ex)}")


	def show(self):
		con = sqlite3.connect(database= "rms.db")
		cur = con.cursor()

		try:
			cur.execute("select * from course")
			rows= cur.fetchall()
			self.coursetable.delete(*self.coursetable.get_children())
			for row in rows:
				self.coursetable.insert('',END, values=row )
		
		except Exception as ex:
			messagebox.showerror("Error", f"Error due to {str(ex)}")

	def search(self):
		con = sqlite3.connect(database= "rms.db")
		cur = con.cursor()

		try:
			cur.execute(f"select * from course where name LIKE '%{self.var_search.get()}%'")
			rows= cur.fetchall()
			self.coursetable.delete(*self.coursetable.get_children())
			for row in rows:
				self.coursetable.insert('',END, values=row )
		
		except Exception as ex:
			messagebox.showerror("Error", f"Error due to {str(ex)}")


if __name__ == "__main__":
	root = Tk()
	obj = courseclass(root)
	root.mainloop()			