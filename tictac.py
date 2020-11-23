def drawField(field):
    for row in range(5):
	    if row%2 == 0:
		    for column in range(5):
		   	    if column%2 == 0:
                    practicalColumn = column/2
                    if column != 4:
			  	 		print(" ",end="")
					else:
			    		print(" ")
				else:
			    	print("|",end="")
		else:
            print("-----")
Player = 1
currentField = [[" "," "," "],[" "," "," "],[" "," "," "]]
while(True):
	print("Players turn: ", Player)
	MoveRow = int(input("Please enter the row\n"))
	MoveColumn = int(input("Please enter the column"))
	if Player == 1:
		#make move for player 1
	   currentField[MoveColumn][MoveRow]= "X"
	   Player = 2
	else:
		#make move for player 1
	   currentField[MoveColumn][MoveRow]="O"
	   Player = 1
	print(currentField)