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
LONG_BREAK_MIN = 10
reps = 0            #reps = repetation
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    my_label.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps         
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        #IF ITS THE 8TH REP:
        count_down(long_break_sec)
        my_label.config(text="BREAK", fg=RED)
    elif reps % 2 == 0:
    #IF ITS THE 2ND/4TH/6TH/8TH REP:
        count_down(short_break_sec)
        my_label.config(text="BREAK", fg=PINK)
    else:
        # IF ITS THE 1ST/3RD/5TH/7TH REP:
        count_down(work_sec)
        my_label.config(text="WORK", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    # convert data type int to string
    if count_sec < 10:
        global timer
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)   #after method is work for time counting as count function
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "✔"
        check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

#label
my_label = Label(text="Timer",fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
my_label.grid(column=1, row=0)
check_mark = Label(text="",fg=GREEN, bg=YELLOW,highlightthickness=0, font=(FONT_NAME, 25))
check_mark.grid(column=1, row=3)

#button
start_button = Button(text="Start", bg="white",highlightthickness=0, font=(FONT_NAME, 10), command=start_timer )
start_button.grid(row=2, column=0)
reset_button = Button(text="Reset", bg="white",highlightthickness=0, font=(FONT_NAME, 10), command=reset_timer)
reset_button.grid(row=2, column=2)

canvas = Canvas(width=200, height=224,bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
window.mainloop()