from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    counter_mins = "00"
    counter_secs = "00"
    canvas.itemconfig(timer_text, text=f'{counter_mins}:{counter_secs}')
    lblTimer.config(text="Timer", fg=GREEN)
    lblSessions.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        lblTimer.config(text="Break", fg=RED)
        countdown(long_break_secs)
    elif reps % 2 == 0:
        lblTimer.config(text="Break", fg=PINK)
        countdown(short_break_secs)
    else:
        lblTimer.config(text="Work", fg=GREEN)
        countdown(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(counter):
    counter_mins = math.floor(counter / 60)
    counter_secs = counter % 60
    if counter_secs < 10:
        counter_secs = f'0{counter_secs}'
    canvas.itemconfig(timer_text, text=f'{counter_mins}:{counter_secs}')
    if counter > 0:
        global timer
        timer = window.after(1000, countdown, counter - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"

        lblSessions.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 20, "bold"))
canvas.grid(row=1, column=1)

lblTimer = Label(text="Timer", font=("Times", 40, "italic"), bg=YELLOW)
lblTimer.config(fg=GREEN)
lblTimer.grid(row=0, column=1)

btnStart = Button(text='start', bg=YELLOW, command=start_timer)
btnStart.grid(row=2, column=0)

btnReset = Button(text='Reset', bg=YELLOW, command=reset_timer)
btnReset.grid(row=2, column=2)

lblSessions = Label(fg=GREEN)
lblSessions.grid(row=3, column=1)

window.mainloop()