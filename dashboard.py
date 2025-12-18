from tkinter import*
import os
from PIL import Image, ImageTk
from course import courseclass
from student import studentclass
from result import resultclass
from report import reportclass
class RMS:
	def __init__(self, root):
		self.root = root
		self.root.title("Student Result Management System")
		self.root.geometry("1350x700+0+0")
		self.root.config(bg="white")
		current_dir = os.path.dirname(__file__)
		img_path = os.path.join(current_dir, "images","logo_p.png")
		self.logo_dash = ImageTk.PhotoImage(file=img_path)
		
		#self.logo_dash=ImageTk.PhotoImage(file="images/logo_p.png")

		title= Label(self.root, text ="Student Result Management System",image = self.logo_dash, compound =LEFT,padx= 10 , font = ("goudy old style", 20, "bold"),bg ="#033054",fg ="white").place(x=0, y=0, relwidth=1, height = 50)

		M_frame = LabelFrame(self.root, text = "Menu", font = ("times new roman",15),bg="white")
		M_frame.place(x=10 , y =70, width= 1340, height= 80)

		btn_course=Button(M_frame, text ="Course", font=("goudy old style",15,"bold"),cursor = "hand2",command = self.add_course,bg = "#0b5377", fg= "white").place(x=20 , y=5, width= 200, height =40)
		btn_student=Button(M_frame, text ="Student", font=("goudy old style",15,"bold"),cursor = "hand2",command= self.add_student,bg = "#0b5377", fg= "white").place(x=240 , y=5, width= 200, height =40)
		btn_result=Button(M_frame, text ="Result", font=("goudy old style",15,"bold"),cursor = "hand2", command= self.add_result,bg = "#0b5377", fg= "white").place(x=460 , y=5, width= 200, height =40)
		btn_view=Button(M_frame, text ="View", font=("goudy old style",15,"bold"),cursor = "hand2",command =self.add_report,bg = "#0b5377", fg= "white").place(x=680 , y=5, width= 200, height =40)
		btn_logout=Button(M_frame, text ="Logout", font=("goudy old style",15,"bold"),cursor = "hand2",bg = "#0b5377", fg= "white").place(x=900 , y=5, width= 200, height =40)
		btn_exit=Button(M_frame, text ="Exit", font=("goudy old style",15,"bold"),cursor = "hand2",bg = "#0b5377", fg= "white").place(x=1120 , y=5, width= 200, height =40)

		self.bg_img =Image.open("images/bg.png")
		self.bg_img =self.bg_img.resize((920,350),Image.LANCZOS)
		self.bg_img = ImageTk.PhotoImage(self.bg_img)

		self.lbl_bg = Label(self.root, image= self.bg_img).place(x=400, y=180, width=920, height= 350)

		self.lbl_course = Label(self.root, text= "Total Courses\n [0]",bd=10,relief = RIDGE, bg= "#e43b06",fg="white" ,font= ("goudy  old style", 15))
		self.lbl_course.place(x= 400, y=530, width=300, height=100)

		self.lbl_student = Label(self.root, text= "Total Students\n [0]",bd=10,relief = RIDGE, bg= "#0676ad",fg="white" ,font= ("goudy  old style", 15))
		self.lbl_student.place(x= 710, y=530, width=300, height=100)

		self.lbl_result = Label(self.root, text= "Total Results\n [0]",bd=10,relief = RIDGE, bg= "#038074",fg="white" ,font= ("goudy  old style", 15))
		self.lbl_result.place(x= 1020, y=530, width=300, height=100)

		footer= Label(self.root, text ="SRMS- Student Result Management System\nContact us for any technical issue 987xxxx32", font = ("goudy old style", 12, "bold"),bg ="#262626",fg ="white").pack(side=BOTTOM,fill = X)

	def add_course(self):
		self.new_win= Toplevel(self.root)
		self.new_obj= courseclass(self.new_win)

	def add_student(self):
		self.new_win= Toplevel(self.root)
		self.new_obj= studentclass(self.new_win)

	def add_result(self):
		self.new_win= Toplevel(self.root)
		self.new_obj= resultclass(self.new_win)

	def add_report(self):
		self.new_win= Toplevel(self.root)
		self.new_obj= reportclass(self.new_win)


if __name__ == "__main__" :

	root = Tk()

	obj = RMS(root)
	root.mainloop()

