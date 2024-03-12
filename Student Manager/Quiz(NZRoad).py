from tkinter import *

names_list = []


class QuizStarter:
    def __init__(self, parent):
        background_color="OldLace"
        #frame set up
        self.quiz_frame = Frame(parent,bg = background_color, padx=100, pady=100)
        self.quiz_frame.grid()

        #Label widget for our heading
        self.heading_label = Label (self.quiz_frame, text = "NZ Road Rules", font=("Tw cen MT", "18", "bold"), bg=background_color)
        self.heading_label.grid(row=0)

        #Label for user name prompt
        self.user_label = Label ( self.quiz_frame, text="Please enter your name below", font=("Tw cen MT", "16", "bold"), bg=background_color)
        self.user_label.grid(row=1)

        #Users input is taken by an entry widget
        self.entry_box=Entry(self.quiz_frame)
        self.entry_box.grid(row=2, pady=20)

        #Continue button
        self.continue_button = Button (self.quiz_frame, text ="Continue", bg="pink", command=self.name_collection)
        self.continue_button.grid(row=3,pady=20)


    def name_collection(self):
        name = self.entry_box.get()
        names_list.append(name)
        print(names_list)
        self.quiz_frame.destroy()
        

#Starting Point of the Page #
if __name__ == "__main__":
    root = Tk()
    root.title("NZ Road Rules Quiz")
    quizStarter_object = QuizStarter(root)
    root.mainloop()#so the window doesn't dissapear.