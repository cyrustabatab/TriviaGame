import tkinter
THEME_COLOR = "#375362"
from quiz_brain import QuizBrain

# TODO allow user to select difficulty and type of questions as well as number of questions

class QuizInterface:

    def __init__(self,quiz_brain: QuizBrain):

        self.quiz_brain = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.configure(bg=THEME_COLOR,padx=20,pady=20)
        self.score_label = tkinter.Label(text="Score: 0",bg=THEME_COLOR,fg='white',font=('Arial',20,'bold'))
        self.score_label.grid(row=0,column=1,sticky=tkinter.E)

        self.canvas = tkinter.Canvas(width=300,height=250,bg='white')
        self.text = self.canvas.create_text(150,125,text="",font=('Arial',20,'italic'),width=280)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        
        self.true_image = tkinter.PhotoImage(file='images/true.png')
        self.false_image = tkinter.PhotoImage(file='images/false.png')

        self.true_button = tkinter.Button(image=self.true_image,command=self._clicked_true)
        self.true_button.grid(row=2,column=0)

        self.false_button = tkinter.Button(image=self.false_image,command=self._clicked_false)
        self.false_button.configure(pady=10)
        self.false_button.grid(row=2,column=1)

        self.reset_button = tkinter.Button(text="PLAY AGAIN!",font=("Arial",40,'normal'),command=self.reset)

        self.reset_button.grid(row=3,column=0,columnspan=2,pady=50)
        self.reset_button.grid_remove()

        self.get_next_question()

        self.window.mainloop()
    ''' 
    def _play_game(self):
        self.score_label = tkinter.Label(text="Score: 0",bg=THEME_COLOR,fg='white',font=('Arial',20,'bold'))
        self.score_label.grid(row=0,column=1,sticky=tkinter.E)

        self.canvas = tkinter.Canvas(width=300,height=250,bg='white')
        self.text = self.canvas.create_text(150,125,text="",font=('Arial',20,'italic'),width=280)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        
        self.true_image = tkinter.PhotoImage(file='images/true.png')
        self.false_image = tkinter.PhotoImage(file='images/false.png')

        self.true_button = tkinter.Button(image=self.true_image,command=self._clicked_true)
        self.true_button.grid(row=2,column=0)

        self.false_button = tkinter.Button(image=self.false_image,command=self._clicked_false)
        self.false_button.configure(pady=10)
        self.false_button.grid(row=2,column=1)

        self.reset_button = tkinter.Button(text="PLAY AGAIN!",font=("Arial",40,'normal'),command=self.reset)

        self.reset_button.grid(row=3,column=0,columnspan=2,pady=50)
        self.reset_button.grid_remove()

        self.get_next_question()


    def _menu(self):

        title_label = tkinter.Label(text="QUIZZLER",bg=THEME_COLOR,fg='black',font=('Arial',20,'bold'))
        title_label.pack()
        
        def start_game():
            title_label.pack_forget()
            play_button.pack_forget()
            self._play_game()
            

        play_button = tkinter.Button(text="PLAY",command=start_game)
        play_button.pack()

        self.window.mainloop()

    '''


    
    def reset(self):
        self.quiz_brain.reset()
        self.reset_button.grid_remove()
        self.true_button.configure(state='active')
        self.false_button.configure(state='active')
        self.score_label['text'] = "Score: 0"
        self.get_next_question()


    def _clicked_true(self):
        
        self.false_button.configure(state='disabled')
        self.true_button.configure(state='disabled')
        correct= self.quiz_brain.check_answer('true')
        self._give_feedback(correct)




    def _clicked_false(self):
        self.false_button.configure(state='disabled')
        self.true_button.configure(state='disabled')
        correct = self.quiz_brain.check_answer('false')
        self._give_feedback(correct)

        

    
    def _give_feedback(self,correct):
        if correct:
            self.canvas.configure(bg='green')
        else:
            self.canvas.configure(bg='red')

        self.window.after(1000,self.get_next_question)


    def get_next_question(self):
        self.canvas.configure(bg='white')
        if self.quiz_brain.still_has_questions():
            self.true_button.config(state='active')
            self.false_button.config(state='active')
            self.clicked = False
            self.score_label['text'] = f"Score: {self.quiz_brain.score}"
            self.canvas.itemconfig(self.text,text=self.quiz_brain.next_question())
        else:
            self.canvas.itemconfig(self.text,text=f"You've reached the end of the quiz!\nFinal Score: {self.quiz_brain.score}/10")
            self.false_button.config(state='disabled')
            self.true_button.config(state='disabled')
            self.reset_button.grid()





