board=[1,2,3,4,5,6,7,8,9]
def game_bord():
    l=' '*14+'*'+'-'*17+'*'
    n=' '*12
    s='  |  '
    print(f"""
{l}
{n}{s}{board[0]}{s}{board[1]}{s}{board[2]}{s}
{l}
{n}{s}{board[3]}{s}{board[4]}{s}{board[5]}{s}
{l}
{n}{s}{board[6]}{s}{board[7]}{s}{board[8]}{s}
{l}
    """)
def play_game():
    while board[0]==1 or board[1]==2 or board[2]==3 or board[3]==4 or board[4]==5 or board[5]==6 or board[6]==7 or board[7]==8 or board[8]==9:
            game_bord()
            ############################################################################################################################################
            player1=int(input("Player1 (X) : Enter num : "))
            while board[player1-1]=="X" or board[player1-1]=="O":
                print()
                print ('-'*100)
                print("                     This field is already reserved")
                print ('-'*100)
                print()
                game_bord()
                player1=int(input("Player1 (X) : Enter num : "))     
            else:
                board[player1-1]="X"         
            ############################################################################################################################################
            if (board[0]=="X" and board[3]=="X" and board[6]=="X") or  (board[1]=="X" and board[4]=="X" and board[7]=="X") or  (board[2]=="X" and board[5]=="X" and board[8]=="X") or  (board[0]=="X" and board[1]=="X" and board[2]=="X") or  (board[3]=="X" and board[4]=="X" and board[5]=="X")or  (board[6]=="X" and board[7]=="X" and board[8]=="X") or  (board[0]=="X" and board[4]=="X" and board[8]=="X") or  (board[2]=="X" and board[4]=="X" and board[6]=="X") :
                game_bord()
                print("--------------------------------------- { Player1 is Winer }--------------------------------------")
                break
            ############################################################################################################################################
            if board[0]==1 or board[1]==2 or board[2]==3 or board[3]==4 or board[4]==5 or board[5]==6 or board[6]==7 or board[7]==8 or board[8]==9:
                game_bord()
                player2=int(input("Player2 (O) : Enter num : "))
                while board[player2-1]=="X" or board[player2-1]=="O":
                    print()
                    print ('-'*100)
                    print("                     This field is already reserved")
                    print ('-'*100)
                    print()
                    game_bord()
                    player2=int(input("Player2 (O) : Enter num : "))
                else:
                    board[player2-1]="O"
                ############################################################################################################################################
                if (board[0]=="O" and board[3]=="O" and board[6]=="O") or  (board[1]=="O" and board[4]=="O" and board[7]=="O") or  (board[2]=="O" and board[5]=="O" and board[8]=="O") or  (board[0]=="O" and board[1]=="O" and board[2]=="O") or  (board[3]=="O" and board[4]=="O" and board[5]=="O")or  (board[6]=="O" and board[7]=="O" and board[8]=="O") or  (board[0]=="O" and board[4]=="O" and board[8]=="O") or  (board[2]=="O" and board[4]=="O" and board[6]=="O") :
                    game_bord()
                    print("--------------------------------------- { Player2 is Winer }----------------------------------------")
                    break      
    else:
        game_bord()
        print()
        print ('-'*100)
        print("                     This places is full")
        print ('-'*100)
        print()
play_game()