from tkinter import *

class QuizStarter:
    def __init__(self, parent):
        background_color="lightpurple"
        #frame set up
        self.quiz_frame = Frame(parent, bg = background_color, padx=100, pady=100)
        self.quiz_frame.grid()

        #Label widget for our heading
        self.heading_label = Label (self.quiz_frame, text = "NZ Road Rules", font=("Tw cen MT", "18", "bold"))
        self.heading_label.grid(row=0)
        

# Starting point of the program #
if __name__ =="_main_":
    root = Tk()
    root.title("NZ Road Rules Quiz")

    root.mainloop()

