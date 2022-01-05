import tkinter

right_side = [4, 4, 4, 4, 4, 4]
right_score = 0
left_side = [4, 4, 4, 4, 4, 4]
left_score = 0

play_screen = tkinter.Tk()

play_screen.title("Mancala")
play_screen.geometry("500x750")

play_screen.columnconfigure(0, weight=1)
play_screen.columnconfigure(1, weight=1)
play_screen.columnconfigure(2, weight=1)
play_screen.columnconfigure(3, weight=1)
play_screen.columnconfigure(4, weight=1)

play_screen.rowconfigure(0, weight=1)
play_screen.rowconfigure(1, weight=1)
play_screen.rowconfigure(2, weight=1)
play_screen.rowconfigure(3, weight=1)
play_screen.rowconfigure(4, weight=1)
play_screen.rowconfigure(5, weight=1)
play_screen.rowconfigure(6, weight=1)
play_screen.rowconfigure(7, weight=1)
play_screen.rowconfigure(8, weight=1)
play_screen.rowconfigure(9, weight=1)
play_screen.rowconfigure(10, weight=1)




padding_frame = tkinter.Frame(play_screen)
padding_frame.grid(row=0, column=0)


right_score_label = tkinter.Label(play_screen, text="Score: {}".format(right_score), relief="groove", bg='light pink')
right_score_label.grid(row=1, column=1, columnspan=3, sticky="nsew")

button_left1 = tkinter.Button(play_screen, text=left_side[0], bg='light steel blue')
button_left1.grid(row=2, column=1, sticky="nsew")

button_left2 = tkinter.Button(play_screen, text=left_side[1], bg='light steel blue')
button_left2.grid(row=3, column=1, sticky="nsew")

button_left3 = tkinter.Button(play_screen, text=left_side[2], bg='light steel blue')
button_left3.grid(row=4, column=1, sticky="nsew")

button_left4 = tkinter.Button(play_screen, text=left_side[3], bg='light steel blue')
button_left4.grid(row=5, column=1, sticky="nsew")

button_left5 = tkinter.Button(play_screen, text=left_side[4], bg='light steel blue')
button_left5.grid(row=6, column=1, sticky="nsew")

button_left6 = tkinter.Button(play_screen, text=left_side[5], bg='light steel blue')
button_left6.grid(row=7, column=1, sticky="nsew")


left_score_label = tkinter.Label(play_screen, text="Score: {}".format(left_score),  relief="groove", bg='light blue')
left_score_label.grid(row=8, column=1, columnspan=3, sticky="nsew")

button_right1 = tkinter.Button(play_screen, text=right_side[0], bg='pink')
button_right1.grid(row=2, column=3, sticky="nsew")

button_right2 = tkinter.Button(play_screen, text=right_side[1], bg='pink')
button_right2.grid(row=3, column=3, sticky="nsew")

button_right3 = tkinter.Button(play_screen, text=right_side[2], bg='pink')
button_right3.grid(row=4, column=3, sticky="nsew")

button_right4 = tkinter.Button(play_screen, text=right_side[3], bg='pink')
button_right4.grid(row=5, column=3, sticky="nsew")

button_right5 = tkinter.Button(play_screen, text=right_side[4], bg='pink')
button_right5.grid(row=6, column=3, sticky="nsew")

button_right6 = tkinter.Button(play_screen, text=right_side[5], bg='pink')
button_right6.grid(row=7, column=3, sticky="nsew")



play_screen.mainloop()

