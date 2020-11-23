def connect4(field):
  for row in range(11):
    if row % 2 == 0:
      practical_row = row // 2
      for column in range(13):
        if column % 2 == 0:
          practical_column = column // 2
          if column != 12:
            print(field[practical_column][practical_row], end="")
          else:
            print(field[practical_column][practical_row])
        else:
          print("|", end="")
    else:
      print("-------------")


player = 1
current_field = [[" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "]
                 ]
connect4(current_field)
while(True):
  print('Players turn: ', player)
  move_column = int(input('Please Enter the column:\n'))
  if player == 1:
    for i in range(1, 7):
      if current_field[move_column][-i] == " ":
        current_field[move_column][-i] = 'X'
        player = 2
        break
  else:
    for i in range(1, 7):
      if current_field[move_column][-i] == " ":
        current_field[move_column][-i] = 'O'
        player = 1
        break
  connect4(current_field)