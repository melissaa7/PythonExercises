import random
from tkinter import *

names_list = []
global questions_answers
asked = []
score=0

questions_answers = {
    1: ["What must you do when you see blue and red flashing lights behind you?",
        'Speed up to get out of the way','Slow down and drive carefully',
        'Slow down and stop','Drive on as usual','Slow down and stop',3],
    2: ["You may stop on motorway only if:",'if there is an emergency',
        'To let down or pick up passengers','to make U-turn',
        'To stop and take a photo','If there is an emegency',1],
    3: ["When coming up to a pedestrian crossing without raised traffic island, what must you do?",
        'Speed up before the pedestrians cross','Stop and give way to pedestrians on any part of the crossing',
        'Sound the horn on your vehicle to warn the pedestrians',
        'Slow down to 30kmh','Stop and give way to pederians on any part of the crossing',2],
    4: ["Can you stop on a bus stop in a private motor vehicle?", 'Only between midnight and 6am',
        'Under no circumstances','when dropping off passengers','Only it it is less than 5 minutes',
        'Under no circumstances',2],
    5: ["What is the maximum speed you may drive if you have a 'space saver wheel' fitted? (km/h)",
        '70 km/h','100 km/h so you do not hold up traffic','80 km/h and if the wheel spacer displays a lower limit that applies',
        '90 km/h','80 km/h and if the wheel spacer displays a lower limit that applies',3],
    6: ["When following another vehicle on a dusty road, you should:",'Speed up to get passed',
        "Turn your vehicle's windscreen wipers on",'Stay back from the dust cloud',
        'Turn your vehicles headlights on', 'Stay back from the dust cloud',3],
    7: ["What does the sign containing the letters 'LSZ' mean",'Low Safety zone', 'Lone star zone', 'Limited speed zone',
        'Limited speed zone',4],
    8: ["What speed are you allowed to pass a school bus that has stopped get on or off?",'20 km/h',
        '30 km/h','70 km/h','10 km/h','20 km/h',1],
    9: ["What is the maximum distance a load may extend in front of a car?",'2 meters forward of the front edge of the front seat',
        '4 meters forward of the front edge of the front seat','3 meters forward of the front seat','2.5 meters forward of the front edge of the front seat',
        '3 meters forward of the front edge of the front seat',3],
    10: ["To avoid being blinded by the headlights of another vehicle coming towards you, what should you do?",
         'Look to the left of the road','look to the center of the road',
         'Wear sunglasses that have sufficient strength','Look to the right side of the road',
         'Look to the left of the road',1]
}

def randomiser():
    global qnum #The question number is the key in our dictionary questions_answers, we have 10 keys
    qnum = random.randint(1,10)
    if qnum not in asked:
        asked.append(qnum)
    elif qnum in asked:
        randomiser()

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
        Quiz(root)

class Quiz:
    def __init__(self, parent):
        background_color="OldLace"
        #frame set up
        self.quiz_frame = Frame(parent,bg = background_color, padx=100, pady=100)
        self.quiz_frame.grid()

        #randomiser will randomly pick a question number which is qnum
        randomiser()

        #Label widget for our heading
        self.question_label = Label (self.quiz_frame, text = questions_answers[qnum][0], font=("Tw cen MT", "18", "bold"), bg=background_color)
        self.question_label.grid(row=0, padx=10, pady=10)

        #holds the value of radio buttons
        self.var1=IntVar()

        #first radio button to hold first choice answer 1
        self.rb1 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][1], font=("Helvetica", "12"), bg="sandybrown", value=1,variable=self.var1, pady=10,padx=10)
        self.rb1.grid(row=1, sticky=W)
        
        #first radio button to hold first choice answer 2
        self.rb2 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][2], font=("Helvetica", "12"), bg="sandybrown", value=2,variable=self.var1, pady=10,padx=10)
        self.rb2.grid(row=2, sticky=W)

        #first radio button to hold first choice answer 3
        self.rb3 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][3], font=("Helvetica", "12"), bg="sandybrown", value=3,variable=self.var1, pady=10,padx=10)
        self.rb3.grid(row=3, sticky=W)

        #first radio button to hold first choice answer 4
        self.rb4 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][4], font=("Helvetica", "12"), bg="sandybrown", value=4,variable=self.var1, pady=10,padx=10)
        self.rb4.grid(row=4, sticky=W)

        #confirm answer button
        self.confirm_button = Button(self.quiz_frame, text="Confirm", bg="pink", command=self.test_progress)
        self.confirm_button.grid(row=5, sticky=W)

        #score label to show score(test result so far)
        self.score_label
    #Method for editing the question label and radio buttons to show the next question data
    def questions_setup(self):
        randomiser()
        self.var1.set(0)
        self.question_label.config(text=questions_answers[qnum][0])
        self.rb1.config(text=questions_answers[qnum][1])
        self.rb2.config(text=questions_answers[qnum][2])
        self.rb3.config(text=questions_answers[qnum][3])
        self.rb4.config(text=questions_answers[qnum][4])

    #This is the method that would get invoked with confirm answer button is clicked, to take care of progress
    def tes_progress(self):
        global score

#Starting Point of the Page #
if __name__ == "__main__":
    root = Tk()
    root.title("NZ Road Rules Quiz")
    quizStarter_object = QuizStarter(root)
    root.mainloop()#so the window doesn't dissapear.