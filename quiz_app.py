import tkinter as tk
from tkinter import messagebox

# QUIZ DATA

quiz_questions = [

    {
        "question": "What is the capital of India?",
        "options": [
            "Delhi",
            "Mumbai",
            "Kolkata",
            "Chennai"
        ],
        "answer": "Delhi"
    },

    {
        "question": "Which language is used for Python development?",
        "options": [
            "Java",
            "Python",
            "HTML",
            "CSS"
        ],
        "answer": "Python"
    },

    {
        "question": "What does CPU stand for?",
        "options": [

            "Central Process Unit",
            "Computer Personal Unit",
            "Central Processing Unit",
            "Control Processing Unit"

        ],
        "answer": "Central Processing Unit"
    },

    {
        "question": "Which symbol is used for comments in Python?",
        "options": [

            "//",
            "#",
            "/* */",
            "&"

        ],
        "answer": "#"
    },

    {
        "question": "Which data structure stores key-value pairs?",
        "options": [

            "List",
            "Tuple",
            "Dictionary",
            "String"

        ],
        "answer": "Dictionary"
    }

]

# VARIABLES

question_index = 0
score = 0
time_left = 15
timer_running = False


# SAVE SCORE

def save_score():

    username = name_entry.get().strip()

    if username == "":
        username = "Anonymous"

    percentage = (
        score /
        len(quiz_questions)
    ) * 100

    with open(
        "scores.txt",
        "a"
    ) as file:

        file.write(

            f"{username} | "
            f"Score: {score}/"
            f"{len(quiz_questions)} | "
            f"{percentage:.2f}%\n"

        )


# FINISH QUIZ

def finish_quiz():

    save_score()

    percentage = (
        score /
        len(quiz_questions)
    ) * 100

    if percentage >= 80:

        result = "Excellent Performance!"

    elif percentage >= 50:

        result = "Good Job!"

    else:

        result = "Keep Practicing!"

    messagebox.showinfo(

        "Quiz Finished",

        f"Name: {name_entry.get()}\n\n"
        f"Score: {score}/"
        f"{len(quiz_questions)}\n"
        f"Percentage: "
        f"{percentage:.2f}%\n\n"
        f"{result}"

    )

    root.destroy()


# NEXT QUESTION

def next_question():

    global question_index
    global score
    global timer_running

    timer_running = False

    if question_index >= len(
        quiz_questions
    ):
        return

    selected = selected_option.get()

    correct_answer = quiz_questions[
        question_index
    ]["answer"]

    if selected == correct_answer:

        score += 1

    question_index += 1

    if question_index < len(
        quiz_questions
    ):

        load_question()

    else:

        finish_quiz()


# TIMER

def update_timer():

    global time_left
    global timer_running

    if not timer_running:
        return

    timer_label.config(

        text=
        f"Time Left: {time_left}s"

    )

    if time_left > 0:

        time_left -= 1

        root.after(
            1000,
            update_timer
        )

    else:

        next_question()


# LOAD QUESTION

def load_question():

    global time_left
    global timer_running

    if question_index >= len(
        quiz_questions
    ):
        return

    timer_running = False

    selected_option.set("")

    time_left = 15

    current = quiz_questions[
        question_index
    ]

    progress_label.config(

        text=
        f"Question "
        f"{question_index+1}"
        f"/"
        f"{len(quiz_questions)}"

    )

    question_label.config(

        text=
        current["question"]

    )

    options = current[
        "options"
    ]

    option1.config(
        text=options[0],
        value=options[0]
    )

    option2.config(
        text=options[1],
        value=options[1]
    )

    option3.config(
        text=options[2],
        value=options[2]
    )

    option4.config(
        text=options[3],
        value=options[3]
    )

    timer_running = True

    update_timer()


# GUI

root = tk.Tk()

root.title(
    "Python Quiz Platform"
)

root.geometry(
    "550x500"
)

title = tk.Label(

    root,

    text=
    "Python Quiz Platform",

    font=(
        "Arial",
        18,
        "bold"
    )

)

title.pack(
    pady=10
)

name_label = tk.Label(

    root,

    text=
    "Enter Name"

)

name_label.pack()

name_entry = tk.Entry(

    root,

    width=25

)

name_entry.pack(
    pady=5
)

progress_label = tk.Label(

    root,

    font=(
        "Arial",
        12
    )

)

progress_label.pack()

timer_label = tk.Label(

    root,

    font=(
        "Arial",
        12
    )

)

timer_label.pack()

question_label = tk.Label(

    root,

    font=(
        "Arial",
        15
    ),

    wraplength=450

)

question_label.pack(
    pady=20
)

selected_option = tk.StringVar()

option1 = tk.Radiobutton(

    root,

    text="",

    variable=
    selected_option,

    value="",

    font=(
        "Arial",
        12
    )

)

option2 = tk.Radiobutton(

    root,

    text="",

    variable=
    selected_option,

    value="",

    font=(
        "Arial",
        12
    )

)

option3 = tk.Radiobutton(

    root,

    text="",

    variable=
    selected_option,

    value="",

    font=(
        "Arial",
        12
    )

)

option4 = tk.Radiobutton(

    root,

    text="",

    variable=
    selected_option,

    value="",

    font=(
        "Arial",
        12
    )

)

option1.pack(
    anchor="w",
    padx=80
)

option2.pack(
    anchor="w",
    padx=80
)

option3.pack(
    anchor="w",
    padx=80
)

option4.pack(
    anchor="w",
    padx=80
)

submit_button = tk.Button(

    root,

    text="Next",

    command=next_question,

    width=10,

    font=(
        "Arial",
        12
    )

)

submit_button.pack(
    pady=20
)

load_question()

root.mainloop()