

global ball_pos
ball_pos = None


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
    global ball_pos
    if ball_pos == None:
        ball_pos = [[-1, -1], [-1, -1]]
    elif ball_pos[1] == [-1, -1]:
        ball_pos[1] = ball_frect.pos
    else:
       ball_pos[0], ball_pos[1] = ball_pos[1], ball_frect.pos

    ball_dir_comps = (ball_pos[1][0] - ball_pos[0][0], ball_pos[1][1] - ball_pos[0][1])

    # ball is travelling towards the paddle
    if ball_dir_comps[0] * (table_size[0]//2 - paddle_frect.pos[0]) < 0:
        dir = "R"
        if ball_dir_comps[0] < 0 and (paddle_frect.pos[0] < other_paddle_frect.pos[0]):
            dir = "L"
        y_pos_pred = y_pos_defence_prediction(paddle_frect, other_paddle_frect, ball_frect, table_size, ball_dir_comps, dir)
        #print(y_pos_pred)
        if paddle_frect.pos[1]+paddle_frect.size[1] < y_pos_pred+ball_frect.size[1]/2:
            return "down"
        else:
            return "up"
        
    # Improving defence. 
    if paddle_frect.pos[1]+paddle_frect.size[1]/2 < table_size[1]/2+ball_frect.size[1]/2:
        return "down"
    else:
        return "up"
    



def y_pos_defence_prediction(paddle_frect, other_paddle_frect, ball_frect, table_size, ball_dir_comps, dir):
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

    return y_pos_pred


