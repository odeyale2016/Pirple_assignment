def drawBoard(rows,cols):
    max_cols = 110
    max_rows = 13
    rows = int(rows)
    cols = int(cols)
    if cols <= max_cols and rows <= max_rows:
        for row in range(rows):
            if row % 2 == 0:
                for col in range(1, cols):
                    if col % 2 == 1:
                        if col != cols - 1:
                            print(" ", end="")
                        else:
                            print(" ")
                    else:
                        print("|", end="")
            else:
                print("-" * cols)
        # After drawing is done return True
        return True
    else:
        # Return False when matrix is not fitting the screen
        reason = ""
        if cols > max_cols and rows > max_rows:
            reason = "columns and rows"
        elif cols > max_cols:
            reason += "columns"
        elif rows > max_rows:
            reason += "rows"
        print("Sorry, cannot create the board, too many {0:s}.".format(reason))
        return False     

drawBoard(19,170)