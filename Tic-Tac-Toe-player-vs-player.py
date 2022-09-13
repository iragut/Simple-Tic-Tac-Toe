game = 0
result = ""
output = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
variable = []
final = False
print(f'''---------
| {output[0]} {output[1]} {output[2]} |
| {output[3]} {output[4]} {output[5]} |
| {output[6]} {output[7]} {output[8]} |
---------''')
while game < 9:
    index = 0
    number = input().split()
    rows = number[0]
    column = number[1]
    counter = False

    while True:              # check if is a number and from 1 to 3
        if not rows.isdigit() and not column.isdigit():
            print("You should enter numbers!")
            break
        elif int(rows) > 3 or int(column) > 3:
            print("Coordinates should be from 1 to 3!")
            break
        else:
            row = int(rows) - 1    # create index for list
            col = int(column) + 2
            index = (row * 3 + col) - 3
            c = 0
            for a in variable:    # check if cell is occupied or not
                if index == a:
                    print("This cell is occupied! Choose another one!")
                    counter = True
                    break

            if counter is True:  # if is occupied break the loop
                break

            for i in output:   # print the result
                if c == index:
                    output.pop(index)
                    if result != "O":
                        output.insert(index, "X")
                        result = "O"
                    else:
                        output.insert(index, "O")
                        result = "X"
                    variable.append(index)
                    c += 1

                    print(f'''---------
| {output[0]} {output[1]} {output[2]} |
| {output[3]} {output[4]} {output[5]} |
| {output[6]} {output[7]} {output[8]} |
---------''')
                    break
                else:
                    c += 1
                             
        if (output[0] + output[1] + output[2]) == "XXX" or (output[3] + output[4] + output[5]) == "XXX" or (output[6] + output[7] + output[8]) == "XXX":   # check who win
            print("X wins")
            final = True
            break
        elif (output[0] + output[3] + output[6]) == "XXX" or (output[1] + output[4] + output[7]) == "XXX" or (output[2] + output[5] + output[8]) == "XXX":
            print("X wins")
            final = True
            break
        elif (output[0] + output[4] + output[8]) == "XXX" or (output[2] + output[4] + output[6]) == "XXX":
            print("X wins")
            final = True
            break
        elif (output[0] + output[3] + output[6]) == "OOO" or (output[1] + output[4] + output[7]) == "OOO" or (output[2] + output[5] + output[8]) == "OOO":
            print("O wins")
            final = True
            break
        elif (output[0] + output[1] + output[2]) == "OOO" or (output[3] + output[4] + output[5]) == "OOO" or (output[6] + output[7] + output[8]) == "OOO":
            print("O wins")
            final = True
            break
        elif (output[0] + output[4] + output[8]) == "OOO" or (output[2] + output[4] + output[6]) == "OOO":
            print("O wins")
            final = True
            break
        else:
            game += 1
            break
    if final:
        break
if game == 9:
    print("Draw")
