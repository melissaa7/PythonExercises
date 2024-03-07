from tkinter import *


class Student:

    def _init_(self,name):
        self.name =name

    def get_grade(self):
        return self.get_grade
    
    def set_grade(self, grade):
        self.grade = grade

def show_grade(event):
    current_cursor = students_listbox.curselection()
    current_student = current_cursor[0]
    grade_label.config(text=csc_2[0].grade)

csc_2 =[]

csc_2.append(Student("Boaz"))
csc_2[0].set_grade("Achieved")

window = Tk()
window.geometry("300x300")

students_listbox = Listbox(window)
students_listbox.pack()

students_listbox.insert(0, "Boaz")

grade_label = Label()
grade_label.pack()

show_grade_btn = Button(text="Show Grade", command=show_grade)
show_grade_btn.pack()

window.mainloop()
