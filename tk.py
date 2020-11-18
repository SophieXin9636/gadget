import tkinter as tk
import os

class Application(object):

	def __init__(self, main_frame):
		tk.Frame.__init__(self, main_frame)
		self.title('File Converter Tools')
		self.geometry('800x600')
		self.configure(background='white')
		self.createBottoms()
		self.pack()

	def createBottoms(self):
		self.btn = tk.Botton(self, 
							 text='File',
							 font=('Arial', 12),
							 width=3,
							 height=1,
							 command=self.)
		self.file_option_list = ("File open", "Save as", "Quit")
		self.file_option_var = tk.StringVar()
		self.file_option_var.set("File")
		self.file_option_menu = tk.OptionMenu(self, 
											  self.file_option_var, 
											 *self.file_option_list) 
		self.file_option_menu.grid(row=5, column=0, sticky=tk.N+tk.W)
		
		self.bottom_frame = tk.Frame(self)
		self.bottom_frame.pack(side=tk.BOTTOM)


window = tk.Tk()
app = Application(window)
window.mainloop()