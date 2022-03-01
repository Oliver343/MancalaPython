from mancala_start import *

# Testing empty 'left_side' triggers endgame
right_side = [4, 4, 4, 4, 4, 4]
left_side = [0, 0, 0, 0, 0, 0]
end_game = False

end_game, right_counter, left_counter = check_end(right_side, left_side)
print("-" * 20)
print("Expected result end_game == True")
if end_game:
    print("Success")
else:
    print("Fail")
print("-" * 20)


# Testing empty 'right_side' triggers endgame
right_side = [0, 0, 0, 0, 0, 0]
left_side = [4, 4, 4, 4, 4, 4]
end_game = False

end_game, right_counter, left_counter = check_end(right_side, left_side)
print("-" * 20)
print("Expected result end_game == True")
if end_game == True:
    print("Success")
else:
    print("Fail")
print("-" * 20)


# Testing edge case situation where everything is empty (can happen after a capture)
right_side = [0, 0, 0, 0, 0, 0]
left_side = [0, 0, 0, 0, 0, 0]
end_game = False

end_game, right_counter, left_counter = check_end(right_side, left_side)
print("-" * 20)
print("Expected result end_game == True")
if end_game == True:
    print("Success")
else:
    print("Fail")
print("-" * 20)
