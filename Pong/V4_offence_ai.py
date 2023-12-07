import math

global ball_pos, ball_dir_comps
ball_pos = None
ball_dir_comps = None



def pong_ai(paddle_frect, other_paddle_frect, ball_frect, table_size):
    '''return "up" or "down", depending on which way the paddle should go to
    align its centre with where it thinks the ball will end up
    
    Arguments:
    paddle_frect: a rectangle representing the coordinates of the paddle
                  paddle_frect.pos[0], paddle_frect.pos[1] is the top-left
                  corner of the rectangle. 
                  paddle_frect.size[0], paddle_frect.size[1] are the dimensions
                  of the paddle along the x and y axis, respectively
    
    other_paddle_frect:
                  a rectangle representing the opponent paddle. It is formatted
                  in the same way as paddle_frect
    ball_frect:   a rectangle representing the ball. It is formatted in the 
                  same way as paddle_frect
    table_size:   table_size[0], table_size[1] are the dimensions of the table,
                  along the x and the y axis respectively
    
    The coordinates look as follows:
    
     0             x
     |------------->
     |
     |             
     |
 y   v
    '''          

    # global variables
    global ball_pos, ball_dir_comps
    if ball_pos == None:
        ball_pos = [[-1, -1], [-1, -1]]
    elif ball_pos[1] == [-1, -1]:
        ball_pos[1] = ball_frect.pos
    else:
       ball_pos[0], ball_pos[1] = ball_pos[1], ball_frect.pos

    if ball_dir_comps == None:
        ball_dir_comps = [0,0]

    if ball_pos[0] == ball_pos[1] and ball_pos[1] != [-1,-1]:
        pass
    else:
        ball_dir_comps = (ball_pos[1][0] - ball_pos[0][0], ball_pos[1][1] - ball_pos[0][1])



    # ball is travelling towards the paddle
    if ball_dir_comps[0] * (table_size[0]//2 - paddle_frect.pos[0]) < 0:
        dir = "R"
        if ball_dir_comps[0] < 0 and (paddle_frect.pos[0] < other_paddle_frect.pos[0]):
            dir = "L"

        y_target = best_y_pos_offence(paddle_frect, other_paddle_frect, ball_frect, table_size, dir)

        if paddle_frect.pos[1]+paddle_frect.size[1]/2 < y_target:
            return "down"
        else:
            return "up"
    


    # Ball is travelling away from paddle
    # Improving defence. 
    if paddle_frect.pos[1]+paddle_frect.size[1]/2 < table_size[1]/2+ball_frect.size[1]/2:
        return "down"
    else:
        return "up"
    



def y_pos_defence_prediction(paddle_frect, other_paddle_frect, ball_frect, table_size, dir):
    global ball_dir_comps
    
    time_to_hit = 0
    
    y_pos_pred = 0
    if ball_dir_comps[0] != 0:
        if dir == "R":
            time_to_hit = abs((paddle_frect.pos[0] - paddle_frect.size[0] - ball_frect.pos[0]) / ball_dir_comps[0])
            y_pos_pred = (ball_pos[1][1] + ball_dir_comps[1] * time_to_hit) % (table_size[1]*2)
            #print(y_pos_pred)
        elif dir == "L":
            time_to_hit = abs((paddle_frect.pos[0] - ball_frect.pos[0]) / ball_dir_comps[0])
            y_pos_pred = (ball_pos[1][1] + ball_dir_comps[1] * time_to_hit) % (table_size[1]*2)
            #print(y_pos_pred)
        else:
            print("Make sure dir in y_pos_predictions is either L or R")
            m += 1
    y_pos_pred = table_size[1] - abs(table_size[1] - y_pos_pred)
    if y_pos_pred > table_size[1]:
       y_pos_pred = table_size[1] - y_pos_pred

    return y_pos_pred + ball_frect.size[1]/2


def best_y_pos_offence(paddle_frect, other_paddle_frect, ball_frect, table_size, dir):
    y_pos_pred = y_pos_defence_prediction(paddle_frect, other_paddle_frect, ball_frect, table_size, dir)
    #print(y_pos_pred)
    possible = False
    # an Ideal spot % table_size is close to 0, within 10 lets say.
    # Identify furthest corner
    # Furthest corner is top one.
    beta = math.atan(abs(ball_dir_comps[1]/ball_dir_comps[0]))
    if ball_dir_comps[1] > 0:
        beta *= -1
    if True: #table_size[1] - other_paddle_frect.pos[1] > (table_size[1]/2):
        alpha1 = math.atan(y_pos_pred/table_size[0])
        alpha2 = -1 * math.atan(((y_pos_pred+table_size[1])/table_size[0]))
        
        pheta1 = (alpha1 + beta)/2
        pheta2 = (alpha2 + beta)/2

        loc1 = y_pos_pred + pheta1*180/math.pi/45*paddle_frect.size[1]/2
        loc2 = y_pos_pred - pheta2*180/math.pi/45*paddle_frect.size[1]/2

        loc = loc2
        #if abs(loc1 - y_pos_pred) < abs(loc2 - y_pos_pred):
            #loc = loc1
        return loc1
    else:
        pass

    
    if dir == "L":
        pass
    # Too hard to implement :(

    if possible:
        pass

    return y_pos_pred+ball_frect.size[1]/2
