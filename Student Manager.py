from tkinter import*

class Student():


    def _init_(self):
        self.first_name = "John"

    def display_name(self):
        print(self.first_name)

    def get_grade(self):
        return self.get_grade
def show_grade():
    #show the grade using a label
    grade_label.config(text=csc_2[0].get_grade())
    pass

csc_2 = []

csc_2.append(Student("Kajah"))
csc_2[0].set_grade("Achieved")

csc_2.append(Student("Boaz"))
csc_2[1].set_grade("Developing")

window = Tk()
window.geometry("300x300")

grade_label = Label()
grade_label.pack()

show_grade_btn = Button(text="Show Grade")
show_grade_btn.pack()

window.mainloop()