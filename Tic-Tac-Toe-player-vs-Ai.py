import random


def output_print(list_output):
    return print(f'''---------
| {list_output[0]} {list_output[1]} {list_output[2]} |
| {list_output[3]} {list_output[4]} {list_output[5]} |
| {list_output[6]} {list_output[7]} {list_output[8]} |
---------''')


game = 0
game_output = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
output_print(game_output)
occupied_cell = []
status = "player"

while game < 9:
    index_map = 0
    if status == "player":
        while True:
            player_input = input("Enter the coordinates:").split()
            if len(player_input) != 2:
                print("You should enter numbers!")
            else:
                rows = player_input[0]
                column = player_input[1]
                break
        counter = False
        
        while True:
            if not rows.isdigit() and not column.isdigit():
                print("You should enter numbers!")
                break
            elif int(rows) > 3 or int(column) > 3:
                print("Coordinates should be from 1 to 3!")
                break
            else:
                index_map = ((int(rows) - 1) * 3 + (int(column) + 2)) - 3

                for a in occupied_cell:
                    if a == index_map:
                        print("This cell is occupied! Choose another one!")
                        counter = True
                        break

                if counter:
                    break
                for i in range(0, len(game_output)):
                    if i == index_map:
                        game_output.pop(i)
                        game_output.insert(i, "X")
                        output_print(game_output)
                        occupied_cell.append(i)
                        break
                game += 1
                status = "computer"
                break
    else:
        computer_choice = random.randint(0, 8)
        if computer_choice in occupied_cell:
            computer_choice = random.randint(0, 8)
        else:
            game_output.pop(computer_choice)
            game_output.insert(computer_choice, "O")
            print("Making move level \"easy\"")
            output_print(game_output)
            occupied_cell.append(computer_choice)
            game += 1
            status = "player"

        if (game_output[0] + game_output[1] + game_output[2]) == "XXX" or (game_output[3] + game_output[4] + game_output[5]) == "XXX" or (game_output[6] + game_output[7] + game_output[8]) == "XXX":
            print("X wins")
            break
        elif (game_output[0] + game_output[3] + game_output[6]) == "XXX" or (game_output[1] + game_output[4] + game_output[7]) == "XXX" or (game_output[2] + game_output[5] + game_output[8]) == "XXX":
            print("X wins")
            break
        elif (game_output[0] + game_output[4] + game_output[8]) == "XXX" or (game_output[2] + game_output[4] + game_output[6]) == "XXX":
            print("X wins")
            break
        elif (game_output[0] + game_output[3] + game_output[6]) == "OOO" or (game_output[1] + game_output[4] + game_output[7]) == "OOO" or (game_output[2] + game_output[5] + game_output[8]) == "OOO":
            print("O wins")
            break
        elif (game_output[0] + game_output[1] + game_output[2]) == "OOO" or (game_output[3] + game_output[4] + game_output[5]) == "OOO" or (game_output[6] + game_output[7] + game_output[8]) == "OOO":
            print("O wins")
            break
        elif (game_output[0] + game_output[4] + game_output[8]) == "OOO" or (game_output[2] + game_output[4] + game_output[6]) == "OOO":
            print("O wins")
            break

if game == 9:
    print("Draw")
