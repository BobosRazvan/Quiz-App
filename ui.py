from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.text_canvas = None
        self.image_true = None
        self.image_false = None
        self.button_right = None
        self.button_wrong = None
        self.canvas = None

        self.window = Tk()
        self.score_label = Label(self.window, text="Score: 0", font=("Arial", 15), bg=THEME_COLOR, fg="#FFFFFF")
        self.configure_window()
        self.initialize_window_components()
        self.get_next_question()
        self.window.mainloop()

    def configure_window(self):
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20)
        self.window.configure(bg=THEME_COLOR)

    def wrong_pressed(self):
        is_wrong = self.quiz.check_answer("False")
        self.give_feedback(is_wrong)

    def right_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg='red')

        self.window.after(1000, self.get_next_question)

    def initialize_window_components(self):
        self.canvas = Canvas(height=250, width=300)
        self.canvas.configure(bg='#FFFFFF')

        self.image_false = PhotoImage(file="images/false.png")
        self.image_true = PhotoImage(file="images/true.png")

        self.button_wrong = Button(self.window, image=self.image_false, command=self.wrong_pressed)
        self.button_right = Button(self.window, image=self.image_true, command=self.right_pressed)

        self.score_label.grid(column=1, row=0)
        self.text_canvas = self.canvas.create_text(150, 100, width=280, text="Salut", font=("Arial", 20, "italic"),
                                                   fill="black")

        self.canvas.grid(column=0, row=1, columnspan=2)
        self.button_wrong.grid(column=0, row=2)
        self.button_right.grid(column=1, row=2)

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text_canvas, text=q_text)
        else:
            self.button_right.config(state="disabled")
            self.button_wrong.config(state="disabled")
            self.canvas.itemconfig(self.text_canvas, text=f"You've reached the end of the quiz. Your final score is {self.quiz.score}/10!")
