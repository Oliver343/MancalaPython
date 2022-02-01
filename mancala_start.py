import tkinter


def button_press(button_id):
    global whos_turn
    global right_side
    global right_score
    global left_side
    global left_score
    drop_side = whos_turn
    drop_pocket = button_id - 1

    if whos_turn:
        side = right_side
    else:
        side = left_side

    temp_holder = side[button_id - 1]
    side[button_id - 1] = 0
    for i in range(temp_holder):
        drop_pocket -= 1
        if drop_pocket < 0:  # Triggered when drop_pocket is less than 0 so is a score space
            drop_pocket = 5
            drop_side = not drop_side
            if side == left_side:
                side = right_side
            else:
                side = left_side
            if drop_side != whos_turn:  # Triggered when current players bean hits score (prevents scoring for other player)
                if whos_turn:
                    right_score += 1
                else:
                    left_score += 1
                print("Score!")

                drop_pocket = 6
            else:
                side[drop_pocket] += 1
            # now check if last bean ended in score pocket
            if i == temp_holder - 1:
                print("another go?")
                swap_turn()
        else:
            side[drop_pocket] += 1

    swap_turn()
    draw_buttons()


def draw_buttons():
    button_left6.grid(row=7, column=1, sticky="nsew")
    button_left6['text']=left_side[0]
    button_left5.grid(row=6, column=1, sticky="nsew")
    button_left5['text']=left_side[1]
    button_left4.grid(row=5, column=1, sticky="nsew")
    button_left4['text']=left_side[2]
    button_left3.grid(row=4, column=1, sticky="nsew")
    button_left3['text']=left_side[3]
    button_left2.grid(row=3, column=1, sticky="nsew")
    button_left2['text']=left_side[4]
    button_left1.grid(row=2, column=1, sticky="nsew")
    button_left1['text']=left_side[5]
    button_right1.grid(row=2, column=3, sticky="nsew")
    button_right1['text']=right_side[0]
    button_right2.grid(row=3, column=3, sticky="nsew")
    button_right2['text']=right_side[1]
    button_right3.grid(row=4, column=3, sticky="nsew")
    button_right3['text']=right_side[2]
    button_right4.grid(row=5, column=3, sticky="nsew")
    button_right4['text']=right_side[3]
    button_right5.grid(row=6, column=3, sticky="nsew")
    button_right5['text']=right_side[4]
    button_right6.grid(row=7, column=3, sticky="nsew")
    button_right6['text']=right_side[5]

    right_score_label = tkinter.Label(play_screen, text="Score: {}".format(right_score), relief="groove", bg='light pink')
    right_score_label.grid(row=1, column=1, columnspan=3, sticky="nsew")

    left_score_label = tkinter.Label(play_screen, text="Score: {}".format(left_score),  relief="groove", bg='light blue')
    left_score_label.grid(row=8, column=1, columnspan=3, sticky="nsew")

    play_screen.mainloop()


def swap_turn():
    global whos_turn
    if whos_turn:
        button_right1["state"] = "disabled"
        button_right2["state"] = "disabled"
        button_right3["state"] = "disabled"
        button_right4["state"] = "disabled"
        button_right5["state"] = "disabled"
        button_right6["state"] = "disabled"
        button_left1["state"] = "active"
        button_left2["state"] = "active"
        button_left3["state"] = "active"
        button_left4["state"] = "active"
        button_left5["state"] = "active"
        button_left6["state"] = "active"
        whos_turn = False
    else:
        button_left1["state"] = "disabled"
        button_left2["state"] = "disabled"
        button_left3["state"] = "disabled"
        button_left4["state"] = "disabled"
        button_left5["state"] = "disabled"
        button_left6["state"] = "disabled"
        button_right1["state"] = "active"
        button_right2["state"] = "active"
        button_right3["state"] = "active"
        button_right4["state"] = "active"
        button_right5["state"] = "active"
        button_right6["state"] = "active"
        whos_turn = True


right_side = [4, 4, 4, 4, 4, 4]  # pink
right_score = 0
left_side = [4, 4, 11, 9, 4, 4]  # blue
left_score = 0
whos_turn = True    # True means its left side / blues turn

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

button_left1 = tkinter.Button(play_screen, text=left_side[0], bg='light steel blue', command=lambda id=6: button_press(id))
button_left2 = tkinter.Button(play_screen, text=left_side[1], bg='light steel blue', command=lambda id=5: button_press(id))
button_left3 = tkinter.Button(play_screen, text=left_side[2], bg='light steel blue', command=lambda id=4: button_press(id))
button_left4 = tkinter.Button(play_screen, text=left_side[3], bg='light steel blue', command=lambda id=3: button_press(id))
button_left5 = tkinter.Button(play_screen, text=left_side[4], bg='light steel blue', command=lambda id=2: button_press(id))
button_left6 = tkinter.Button(play_screen, text=left_side[5], bg='light steel blue', command=lambda id=1: button_press(id))

left_score_label = tkinter.Label(play_screen, text="Score: {}".format(left_score),  relief="groove", bg='light blue')
left_score_label.grid(row=8, column=1, columnspan=3, sticky="nsew")

button_right1 = tkinter.Button(play_screen, text=right_side[0], bg='pink', command=lambda id=1: button_press(id))
button_right2 = tkinter.Button(play_screen, text=right_side[1], bg='pink', command=lambda id=2: button_press(id))
button_right3 = tkinter.Button(play_screen, text=right_side[2], bg='pink', command=lambda id=3: button_press(id))
button_right4 = tkinter.Button(play_screen, text=right_side[3], bg='pink', command=lambda id=4: button_press(id))
button_right5 = tkinter.Button(play_screen, text=right_side[4], bg='pink', command=lambda id=5: button_press(id))
button_right6 = tkinter.Button(play_screen, text=right_side[5], bg='pink', command=lambda id=6: button_press(id))

swap_turn()
draw_buttons()
