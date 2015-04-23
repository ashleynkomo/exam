# Skeleton Program code for the AQA COMP1 Summer 2015 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA COMP1 Programmer Team
# developed in the Python 3.4 programming environment

BOARDDIMENSION = 8

def display_menu():
  print("Main Menu")
  print()
  print("1. Start new game")
  print("2. Load existing game")
  print("3. Play sample game")
  print("4. View high score")
  print("5. Settings")
  print("6. Quit program")
  print()


def get_menu_selection():
  menu_choice = int(input("Please select an option from the menu: "))
  print()
  return menu_choice
 
def make_selection(menu_choice, play_game):
  if menu_choice == 1:
    SampleGame = "N"
    play_game(SampleGame)
  if menu_choice == 2:
    print("2")
  if menu_choice == 3:
    SampleGame = "Y"
    play_game(SampleGame)
  if menu_choice == 4:
    print("4")
  if menu_choice == 5:
    print("5")
  if menu_choice == 6:
    print("Exited")
    quit 


def in_game_menu():
  print()
  print("Options")
  print()
  print("1. Save Game")
  print("2. Quit to Menu")
  print("3. Return to Game")
  print("4. Surrender")
  print()
  option = int(input("Please select an option: "))
  return option

def CreateBoard():
  Board = []
  for Count in range(BOARDDIMENSION + 1):
    Board.append([])
    for Count2 in range(BOARDDIMENSION + 1):
      Board[Count].append("  ")
  return Board

def DisplayWhoseTurnItIs(WhoseTurn):
  if WhoseTurn == "W":
    print("It is White's turn")
  else:
    print("It is Black's turn")

def GetTypeOfGame():
  TypeOfGame = input("Do you want to play the sample game (enter Y for Yes)? ")
  TypeOfGame = TypeOfGame.lower()[0]
  return TypeOfGame

def DisplayWinner(WhoseTurn): 
  if WhoseTurn == "W":
    print("Black's Sarrum has been captured.  White wins!")
  else:
    print("White's Sarrum has been captured.  Black wins!")

def CheckIfGameWillBeWon(Board, FinishRank, FinishFile):
  if Board[FinishRank][FinishFile][1] == "S":
    return True
  else:
    return False

def DisplayBoard(Board):
  print()
  for RankNo in range(1, BOARDDIMENSION + 1):
    print("     -------------------------")
    print("R"+str(RankNo), end="   ")
    for FileNo in range(1, BOARDDIMENSION + 1):
      print("|" + Board[RankNo][FileNo], end="")
    print("|")
  print("     -------------------------")
  print()
  print("      F1 F2 F3 F4 F5 F6 F7 F8")
  print()
  print()    

def CheckRedumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, ColourOfPiece): 
  CheckRedumMoveIsLegal = False
  if ColourOfPiece == "W":
    if FinishRank == StartRank - 1:
      if FinishFile == StartFile and Board[FinishRank][FinishFile] == "  ":
        CheckRedumMoveIsLegal = True
      elif abs(FinishFile - StartFile) == 1 and Board[FinishRank][FinishFile][0] == "B":
        CheckRedumMoveIsLegal = True
  elif FinishRank == StartRank + 1:
    if FinishFile == StartFile and Board[FinishRank][FinishFile] == "  ":
      CheckRedumMoveIsLegal = True
    elif abs(FinishFile - StartFile) == 1 and Board[FinishRank][FinishFile][0] == "W":
      CheckRedumMoveIsLegal = True
  return CheckRedumMoveIsLegal

def CheckSarrumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile): 
  CheckSarrumMoveIsLegal = False
  if abs(FinishFile - StartFile) <= 1 and abs(FinishRank - StartRank) <= 1:
    CheckSarrumMoveIsLegal = True
  return CheckSarrumMoveIsLegal

def CheckGisgigirMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile): 
  GisgigirMoveIsLegal = False
  RankDifference = FinishRank - StartRank
  FileDifference = FinishFile - StartFile
  if RankDifference == 0:
    if FileDifference >= 1:
      GisgigirMoveIsLegal = True
      for Count in range(1, FileDifference):
        if Board[StartRank][StartFile + Count] != "  ":
          GisgigirMoveIsLegal = False
    elif FileDifference <= -1:
      GisgigirMoveIsLegal = True
      for Count in range(-1, FileDifference, -1):
        if Board[StartRank][StartFile + Count] != "  ":
          GisgigirMoveIsLegal = False
  elif FileDifference == 0:
    if RankDifference >= 1:
      GisgigirMoveIsLegal = True
      for Count in range(1, RankDifference):
        if Board[StartRank + Count][StartFile] != "  ":
          GisgigirMoveIsLegal = False
    elif RankDifference <= -1:
      GisgigirMoveIsLegal = True
      for Count in range(-1, RankDifference, -1):
        if Board[StartRank + Count][StartFile] != "  ":
          GisgigirMoveIsLegal = False
  return GisgigirMoveIsLegal

def CheckNabuMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckNabuMoveIsLegal = False
  if abs(FinishFile - StartFile) == abs(FinishRank - StartRank):
    CheckNabuMoveIsLegal = True
  Change = FinishRank - StartRank #Create new variable for calculating the difference
  if Change >= 1:
    CheckNabuMoveIsLegal = True
    Count = 1
    while count != Change:
      if Board[StartRank + Count][StartFile + Count] != "  ":
        CheckNabuMoveIsLegal = False
      Count += 1
  elif Change <= -1:
    CheckNabuMoveIsLegal = True
    Count = -1
    while Count != Difference:
      if Board[StartRank + Count][StartFile + Count] != "  ":
        CheckNabuMoveIsLegal = False
    
  
  return CheckNabuMoveIsLegal

def CheckMarzazPaniMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):#abs means Return the absolute value of a number
  CheckMarzazPaniMoveIsLegal = False
  if (abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 0) or (abs(FinishFile - StartFile) == 0 and abs(FinishRank - StartRank) ==1) or (abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) ==1):#ADDED ANOTHER OR EXCEPT A 1 INSTEAD OF 0 :
    CheckMarzazPaniMoveIsLegal = True
  return CheckMarzazPaniMoveIsLegal


def CheckEtluMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile): 
  CheckEtluMoveIsLegal = False
  if (abs(FinishFile - StartFile) == 2 and abs(FinishRank - StartRank) == 1) or (abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 2):#Changed 0 to 1
    CheckEtluMoveIsLegal = True
  return CheckEtluMoveIsLegal

def CheckMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn): 
  MoveIsLegal = True
  try:
    if (FinishFile == StartFile) and (FinishRank == StartRank):
      MoveIsLegal = False
    elif FinishRank == 0: 
      MoveIsLegal = False
    elif FinishFile == 0:
      MoveIsLegal = False
    else:
      PieceType = Board[StartRank][StartFile][1]
      PieceColour = Board[StartRank][StartFile][0]
      if WhoseTurn == "W":
        if PieceColour != "W":
          MoveIsLegal = False
        if Board[FinishRank][FinishFile][0] == "W":
          MoveIsLegal = False
      else:
        if PieceColour != "B":
          MoveIsLegal = False
        if Board[FinishRank][FinishFile][0] == "B":
          MoveIsLegal = False
      if MoveIsLegal == True:
        if PieceType == "R":
          MoveIsLegal = CheckRedumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, PieceColour)
        elif PieceType == "S":
          MoveIsLegal = CheckSarrumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
        elif PieceType == "M":
          MoveIsLegal = CheckMarzazPaniMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
        elif PieceType == "G":
          MoveIsLegal = CheckGisgigirMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
        elif PieceType == "N":
          MoveIsLegal = CheckNabuMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
        elif PieceType == "E":
          MoveIsLegal = CheckEtluMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
    
  except IndexError: 
    MoveIsLegal = False
  return MoveIsLegal

def InitialiseBoard(Board, SampleGame):
    if SampleGame == "Y":
        InitialiseSampleBoard(Board)
    else:
        InitialiseNewBoard(Board)
        
def InitialiseSampleBoard(Board):
    for RankNo in range(1, BOARDDIMENSION + 1):
      for FileNo in range(1, BOARDDIMENSION + 1):
        Board[RankNo][FileNo] = "  "
    Board[1][2] = "BG"
    Board[1][4] = "BS"
    Board[1][8] = "WG"
    Board[2][1] = "WR"
    Board[3][1] = "WS"
    Board[3][2] = "BE"
    Board[3][8] = "BE"
    Board[6][8] = "BR"
    
def InitialiseNewBoard(Board):
    for RankNo in range(1, BOARDDIMENSION + 1):
      for FileNo in range(1, BOARDDIMENSION + 1):
        if RankNo == 2:
          Board[RankNo][FileNo] = "BR"
        elif RankNo == 7:
          Board[RankNo][FileNo] = "WR"
        elif RankNo == 1 or RankNo == 8:
          if RankNo == 1:
            Board[RankNo][FileNo] = "B"
          if RankNo == 8:
            Board[RankNo][FileNo] = "W"
          if FileNo == 1 or FileNo == 8:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "G"
          elif FileNo == 2 or FileNo == 7:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "E"
          elif FileNo == 3 or FileNo == 6:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "N"
          elif FileNo == 4:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "M"
          elif FileNo == 5:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "S"
        else:
          Board[RankNo][FileNo] = "  "   
                    
def GetMove(StartSquare, FinishSquare, WhoseTurn): 
  try:
    Confirmed = False
    Surrender = False
    Exit = False
    while not Confirmed:
      StartSquare = int(input("Enter coordinates of square containing piece to move (file first) or type '-1' for menu: "))
      if StartSquare == -1:
        option = in_game_menu()
        if option == 1:
          print("Game Saved")
          Confirmed = True
          Exit = True
        elif option == 2:
          Exit = True
          Confirmed = True
          return StartSquare, FinishSquare, Exit
        elif option == 4:
          if WhoseTurn == "W":
            print("Surrendering...")
            print()
            print("White surrenderederd. Black wins!")
            Surrender = True
          else:
            print("Surrendering...")
            print()
            print("Black surrenderederd. White wins!")
            Surrender = True
          Exit = True
          Confirmed = True
        else:
          Exit = False
      else: 
        StartSquareLength = len(str(StartSquare))
        if StartSquareLength <2:
          print("Please provide both FILE and RANK for this move")
        else:
          Confirmed = True
  except ValueError:
    print("you must enter the coordinates in in integer form")
  try:
    FinishConfirmed = False
    while not FinishConfirmed:
      FinishSquare = int(input("Enter coordinates of square to move piece to (file first): "))
      FinishSquareLength = len(str(FinishSquare))
      if FinishSquareLength <2:
        print("Please provide both FILE and RANK for this move")
      else:
        FinishConfirmed = True
  except ValueError:
    print("You must enter the coordinates in integer form")
  return StartSquare, FinishSquare

def MakeMove(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn): 
  if WhoseTurn == "W" and FinishRank == 1 and Board[StartRank][StartFile][1] == "R":
    print("White Redum promoted to Marzaz Pani.")
    Board[FinishRank][FinishFile] = "WM"
    Board[StartRank][StartFile] = "  "
  elif WhoseTurn == "B" and FinishRank == 8 and Board[StartRank][StartFile][1] == "R":
    print("Black Redum Promoted to Marzaz Pani.")
    Board[FinishRank][FinishFile] = "BM"
    Board[StartRank][StartFile] = "  "
  else:
    GetPieceName(Board, StartRank, StartFile, FinishRank, FinishFile,WhoseTurn)
    Board[FinishRank][FinishFile] = Board[StartRank][StartFile]
    Board[StartRank][StartFile] = "  "

def ConfirmMove(StartSquare,FinishSquare): 
  StartRank = StartSquare % 10
  StartFile = StartSquare // 10
  FinishRank = FinishSquare % 10
  FinishFile = FinishSquare // 10
  print()
  print("Move from Rank {0}, File {1} to Rank {2}, File {3}?".format(StartRank, StartFile, FinishRank,FinishFile))
  ConfirmMove = input("Confirm move (yes/no): ")
  ConfirmMove = ConfirmMove.lower()[0]
  if ConfirmMove == "y":
    Confirmed = True
  elif ConfirmMove == "n":
    Confirmed = False
  else:
    print()
    print("You must enter a valid response to confirm your move")
    Confirmed = ConfirmMove(StartSquare, FinishSquare)
  return Confirmed

def GetPieceName(Board, StartRank, StartFile, FinishRank, FinishFile,WhoseTurn): 
  if WhoseTurn == "W":
    ColourPiece = "White"
    TakenPiece = "Black"
  else:
    ColourPiece = "Black"
    TakenPiece = "White"
  if Board[StartRank][StartFile][1] == "R":
    PlayerPiece = "Redum"
  elif Board[StartRank][StartFile][1] == "S":
    PlayerPiece = "Sarrum"
  elif Board[StartRank][StartFile][1] == "E":
    PlayerPiece = "Etlu"
  elif Board[StartRank][StartFile][1] == "G":
    PlayerPiece = "Gisgigir"
  elif Board[StartRank][StartFile][1] == "N":
    PlayerPiece = "Nabu"
  else:
    PlayerPiece = "Marzaz pani"
  if Board[FinishRank][FinishFile][1] == "R":
    FinishPlayerPiece = "Redum"
  elif Board[FinishRank][FinishFile][1] == "S":
    FinishPlayerPiece = "Sarrum"
  elif Board[FinishRank][FinishFile][1] == "E":
    FinishPlayerPiece = "Etlu"
  elif Board[FinishRank][FinishFile][1] == "G":
    FinishPlayerPiece = "Gisgigir"
  elif Board[FinishRank][FinishFile][1] == "N":
    FinishPlayerPiece = "Nabu"
  elif Board[FinishRank][FinishFile][1] == "M":
    FinishPlayerPiece = "Marzaz pani"
  else:
    FinishPlayerPiece = " "
  if FinishPlayerPiece == " ":
    print()
  else:
    print()
    print("{0} {1} takes {2} {3}".format(ColourPiece, PlayerPiece, TakenPiece, FinishPlayerPiece))


  
def play_game(SampleGame):
  StartSquare = 0 
  FinishSquare = 0
  WhoseTurn = "W"
  GameOver = False
  if ord(SampleGame) >= 97 and ord(SampleGame) <= 122:
    SampleGame = chr(ord(SampleGame) - 32)
    
  InitialiseBoard(Board, SampleGame)
  while not(GameOver):
    DisplayBoard(Board)
    DisplayWhoseTurnItIs(WhoseTurn)
    MoveIsLegal = False
    skip = False
    while not(MoveIsLegal):
      StartSquare, FinishSquare  = GetMove(StartSquare, FinishSquare, WhoseTurn)
      if Quit == True:
        return 
      Confirmed = ConfirmMove(StartSquare,FinishSquare)
      if Confirmed == "y":
        StartRank = StartSquare % 10
        StartFile = StartSquare // 10
        FinishRank = FinishSquare % 10
        FinishFile = FinishSquare // 10
        MoveIsLegal = CheckMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn)
        if not(MoveIsLegal)and Confirmed:
          print("That is not a legal move - please try again")
    GameOver = CheckIfGameWillBeWon(Board, FinishRank, FinishFile)
    MakeMove(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn)
    if GameOver:
      DisplayWinner(WhoseTurn)
    if WhoseTurn == "W":
      WhoseTurn = "B"
    else:
      WhoseTurn = "W"
  PlayAgain = input("Do you want to play again (enter Y for Yes)? ")
  if ord(PlayAgain) >= 97 and ord(PlayAgain) <= 122:
    PlayAgain = chr(ord(PlayAgain) - 32)

if __name__ == "__main__":
  Board = CreateBoard()
  PlayAgain = "Y"
  while PlayAgain == "Y":
    display_menu()
    menu_choice = get_menu_selection()
    make_selection(menu_choice,play_game)
    
  
# refactoring is the process of making a piece of code more efficient and easier to understand.
