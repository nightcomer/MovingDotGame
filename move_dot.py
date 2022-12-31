import tkinter as tk
import keyboard as k

# main window
window = tk.Tk()
window.title("Dot Game")
canvas = tk.Canvas(width=500, height=500, background='white')
canvas.grid(row=2, column=1)

# dot
dot_x = 250
dot_y = 250
dot = canvas.create_oval(dot_x-5, dot_y-5, dot_x+5, dot_y+5, fill="blue")

# move dot up
def move_up():
    global dot_y
    if dot_y > 5:
        dot_y -= 5
        canvas.move(dot, 0, -5)

# move dot down
def move_down():
    global dot_y
    if dot_y < 295:
        dot_y += 5
        canvas.move(dot, 0, 5)

# move dot left
def move_left():
    global dot_x
    if dot_x > 5:
        dot_x -= 5
        canvas.move(dot, -5, 0)

# move dot right
def move_right():
    global dot_x
    if dot_x < 295:
        dot_x += 5
        canvas.move(dot, 5, 0)


# arrow key functionality
k.add_hotkey("up", move_up)
k.add_hotkey("down", move_down)
k.add_hotkey("left", move_left)
k.add_hotkey("right", move_right)

# exit button
exit_button = tk.Button(window, text="Exit", width=10, command=lambda: exit())
exit_button.grid(row=3, column=1)

window.mainloop()