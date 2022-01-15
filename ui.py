from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ('Arial', 20, 'italic')


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text='Score: 0', bg=THEME_COLOR, fg='white')
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.quiz_text = self.canvas.create_text(150, 125, text='hello', font=FONT, fill=THEME_COLOR, width=280)
        self.canvas.grid(columnspan=2, column=0, row=1, pady=50)

        true_image = PhotoImage(file='images/true.png')
        self.true_button = Button(image=true_image, bg=THEME_COLOR, highlightthickness=0,
                                  command=self.answered_true)
        self.true_button.grid(column=0, row=2)

        false_image = PhotoImage(file='images/false.png')
        self.false_button = Button(image=false_image, bg=THEME_COLOR, highlightthickness=0,
                                   command=self.answered_false)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quiz_text, text=q_text)
        else:
            self.canvas.itemconfig(self.quiz_text, text="You've reached the end of the quiz.")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def answered_true(self):
        is_right = self.quiz.check_answer('true')
        self.give_feedback(is_right)

    def answered_false(self):
        is_right = self.quiz.check_answer('false')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='Green')
        if not is_right:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)



