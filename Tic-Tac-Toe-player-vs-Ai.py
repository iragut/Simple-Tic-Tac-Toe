import random


def output_print(list_output):
    return print(f'''---------
| {list_output[0]} {list_output[1]} {list_output[2]} |
| {list_output[3]} {list_output[4]} {list_output[5]} |
| {list_output[6]} {list_output[7]} {list_output[8]} |
---------''')


def winning(data_list):
    if (data_list[0] + data_list[1] + data_list[2]) == "XXX" or (
            data_list[3] + data_list[4] + data_list[5]) == "XXX" or (
            data_list[6] + data_list[7] + data_list[8]) == "XXX":
        print("X wins")
        return True
    elif (data_list[0] + data_list[3] + data_list[6]) == "XXX" or (
            data_list[1] + data_list[4] + data_list[7]) == "XXX" or (
            data_list[2] + data_list[5] + data_list[8]) == "XXX":
        print("X wins")
        return True
    elif (data_list[0] + data_list[4] + data_list[8]) == "XXX" or (
            data_list[2] + data_list[4] + data_list[6]) == "XXX":
        print("X wins")
        return True
    elif (data_list[0] + data_list[3] + data_list[6]) == "OOO" or (
            data_list[1] + data_list[4] + data_list[7]) == "OOO" or (
            data_list[2] + data_list[5] + data_list[8]) == "OOO":
        print("O wins")
        return True
    elif (data_list[0] + data_list[1] + data_list[2]) == "OOO" or (
            data_list[3] + data_list[4] + data_list[5]) == "OOO" or (
            data_list[6] + data_list[7] + data_list[8]) == "OOO":
        print("O wins")
        return True
    elif (data_list[0] + data_list[4] + data_list[8]) == "OOO" or (
            data_list[2] + data_list[4] + data_list[6]) == "OOO":
        print("O wins")
        return True


class PlayerVsAi:
    def __init__(self, difficulty):
        game = 0
        game_output = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
        output_print(game_output)
        occupied_cell = []
        status = "player"

        while game < 9:
            if status == "player":
                while True:
                    player_input = input("Enter the coordinates:").split()
                    if len(player_input) != 2:
                        print("You should enter numbers!")
                    else:
                        rows = player_input[0]
                        column = player_input[1]
                        counter = False
                        break

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
                if difficulty == "easy":
                    while True:
                        computer_choice = random.randint(0, 8)
                        if computer_choice in occupied_cell:
                            pass
                        else:
                            game_output.pop(computer_choice)
                            game_output.insert(computer_choice, "O")
                            print("Making move level \"easy\"")
                            output_print(game_output)
                            occupied_cell.append(computer_choice)
                            game += 1
                            status = "player"
                            break

                elif difficulty == "medium":
                    computer_choice = (2 if (game_output[0] + game_output[1] + game_output[2]) == "XX_"
                                       else 1 if game_output[0] + game_output[1] + game_output[2] == "X_X"
                                       else 0 if game_output[0] + game_output[1] + game_output[2] == "_XX"
                                       else 5 if game_output[3] + game_output[4] + game_output[5] == "XX_"
                                       else 4 if game_output[3] + game_output[4] + game_output[5] == "X_X"
                                       else 3 if game_output[3] + game_output[4] + game_output[5] == "_XX"
                                       else 8 if game_output[6] + game_output[7] + game_output[8] == "XX_"
                                       else 7 if game_output[6] + game_output[7] + game_output[8] == "X_X"
                                       else 6 if game_output[6] + game_output[7] + game_output[8] == "_XX"

                                       else 6 if game_output[0] + game_output[3] + game_output[6] == "XX_"
                                       else 3 if game_output[0] + game_output[3] + game_output[6] == "X_X"
                                       else 0 if game_output[0] + game_output[3] + game_output[6] == "_XX"
                                       else 7 if game_output[1] + game_output[4] + game_output[7] == "XX_"
                                       else 4 if game_output[1] + game_output[4] + game_output[7] == "X_X"
                                       else 1 if game_output[1] + game_output[4] + game_output[7] == "_XX"
                                       else 8 if game_output[2] + game_output[5] + game_output[8] == "XX_"
                                       else 5 if game_output[2] + game_output[5] + game_output[8] == "X_X"
                                       else 2 if game_output[2] + game_output[5] + game_output[8] == "_XX"

                                       else 8 if game_output[0] + game_output[4] + game_output[8] == "XX_"
                                       else 4 if game_output[0] + game_output[4] + game_output[8] == "X_X"
                                       else 0 if game_output[0] + game_output[4] + game_output[8] == "_XX"
                                       else 6 if (game_output[2] + game_output[4] + game_output[6]) == "XX_"
                                       else 4 if (game_output[2] + game_output[4] + game_output[6]) == "X_X"
                                       else 2 if (game_output[2] + game_output[4] + game_output[6]) == "_XX" else random.randint(0, 8))

                    while True:
                        if computer_choice in occupied_cell:
                            computer_choice = random.randint(0, 8)
                        else:
                            game_output.pop(computer_choice)
                            game_output.insert(computer_choice, "O")
                            print("Making move level \"medium\"")
                            output_print(game_output)
                            occupied_cell.append(computer_choice)
                            game += 1
                            status = "player"
                            break

                if winning(game_output):
                    break

        if game == 9:
            print("Draw")


while True:
    input_command = input("Input command:").split()
    if input_command[0] == "exit":
        break
    elif len(input_command) < 3:
        print("Bad parameters!")
    elif "easy" in input_command:
        PlayerVsAi("easy")
    elif "medium" in input_command:
        PlayerVsAi("medium")

