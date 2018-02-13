board=[0,0,0,
       0,0,0,
       0,0,0]

def show():
    print board[0],"|",board[1],"|",board[2]
    print "-------------"
    print board[3],"|",board[4],"|",board[5]
    print "-------------"
    print board[6],"|",board[7],"|",board[8]
    print "-------------"

while True:
    x=int(input("player_1:enter spot (0,8)    "))
    if board[x]!=(0):
        print("sorry!!this spot is taken   ")
    else:
        y=int(input("player_1:enter odd num (1,9)  "))
        board[x]=(y)

        show()

        sum_1=board[0]+board[1]+board[2]
        sum_2=board[3]+board[4]+board[5]
        sum_3=board[6]+board[7]+board[8]
        sum_4=board[0]+board[3]+board[6]
        sum_5=board[1]+board[4]+board[7]
        sum_6=board[2]+board[5]+board[8]
        sum_7=board[0]+board[4]+board[8]
        sum_8=board[2]+board[4]+board[6]

        if sum_1==15 or sum_2==15 or sum_3==15 or sum_4==15 or sum_5==15 or sum_6==15 or sum_6==15 or sum_7==15 or sum_8==15:
            print("player_1 is winer   ")
            
            break;
        else:
            
                z=int(input("player_2:enter spot(0,8)   "))
                if board[z]!=(0):
                    print("sorry!!this spot is taken   ")
                else:
                    m=int(input("player_2:enter even num (1,9)  "))
                    board[z]=(m)
                    
                    sum_1=board[0]+board[1]+board[2]
                    sum_2=board[3]+board[4]+board[5]
                    sum_3=board[6]+board[7]+board[8]
                    sum_4=board[0]+board[3]+board[6]
                    sum_5=board[1]+board[4]+board[7]
                    sum_6=board[2]+board[5]+board[8]
                    sum_7=board[0]+board[4]+board[8]
                    sum_8=board[2]+board[4]+board[6]
        
                    if sum_1==15 or sum_2==15 or sum_3==15 or sum_4==15 or sum_5==15 or sum_6==15 or sum_7==15  or sum_8==15:
                        print("player_2 is winer   ")

                        break;

                show()
                    
                
               
            
