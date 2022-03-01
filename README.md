# MancalaPython
Mancala testing project.

A simple implementation of the two player game Mancala.
The number on each button is referred to as beans and the button as a pocket\
as is the case with the mancala game.

Typically the game starts with each player having 4 beans in each pocket but\
I will usually change this number during testing. This can be adjusted by\
changing the numbers in the lists 'right_side' and 'left_side'

A personal project in order to familiarize myself with Python coding.


##LINKED DATA

mancala_data.json is the data file for mancala_start.py
It currently holds button colour information.


##LAYOUT

The user interface is created using the tkinter grid geometry manager that is\
redrawn after the user input to reflex the changes.

The interface is a 5 * 11 grid as displayed below:

    [  ][  ][  ][  ][  ]
    [  ][RS][RC][RC][  ]
    [  ][L6][WL][R1][  ]
    [  ][L5][WC][R2][  ]
    [  ][L4][WC][R3][  ]
    [  ][L3][WC][R4][  ]
    [  ][L2][  ][R5][  ]
    [  ][L1][  ][R6][  ]
    [  ][LS][LC][LC][  ]
    [  ][  ][  ][  ][  ]
    [  ][  ][  ][  ][  ]

**Key:**\
* WL = winner_label\
* WC = winner_label (additional row span)\
* RS = right_score_label\
* RC = right_score_label (additional column span)\
* LS = left_score_label\
* LC = left_score_label (additional column span)\
* R1 = button_right1\
* R2 = button_right2\
* R3 = button_right3\
* R4 = button_right4\
* R5 = button_right5\
* R6 = button_right6\
* L1 = button_left1\
* L2 = button_left2\
* L3 = button_left3\
* L4 = button_left4\
* L5 = button_left5\
* L6 = button_left6\


#ISSUES

There is a known issue with the 'capture_pocket' function where it\
can still happen on the opponents side that needs to be addressed.


#FUTURE UPDATES

More testing is required on this build.

Eventually I plan to start implementing a basic computer opponent\
that can be used for solo play.

