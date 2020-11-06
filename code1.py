
from tkinter import *
import numpy as np

# for initialization and refresh board
size_of_board = 400
number_of_dots = 4
symbol_size = (size_of_board / 3 - size_of_board / 8) / 2
symbol_thickness = 50
#colors
dot_color = '#7BC043'
player1_color = '#0492CF'
player1_color_light = '#67B0CF'
player2_color = '#EE4035'
player2_color_light = '#EE7E77'
Green_color = '#7BC043'
dot_width = 0.25*size_of_board/number_of_dots#big dot width
edge_width = 0.1*size_of_board/number_of_dots#edges
distance_between_dots = size_of_board / (number_of_dots)#distance b/w dots

class Dots_and_Boxes():

    reset_board = False
    player1_turn = True
    
    board_status = np.zeros(shape=(number_of_dots - 1, number_of_dots - 1))
    row_status = np.zeros(shape=(number_of_dots, number_of_dots - 1))
    col_status = np.zeros(shape=(number_of_dots - 1, number_of_dots))
    def __init__(self):
        self.window = Tk()
        self.window.title('Dots_and_Boxes')
        self.canvas = Canvas(self.window, width=size_of_board, height=size_of_board)
        self.canvas.pack()
        self.window.bind('<Button-1>', self.click)
        self.player1_starts = True
        self.refresh_board()
        # self.play_again()

    # on click on edges
    def click(self, event):
        if not self.reset_board:
            grid_position = [event.x, event.y] 
            logical_positon, valid_input = self.convert_grid_to_logical_position(grid_position)
            
    # To check whether grid occupied or not
    def is_grid_occupied(self, logical_position, type):
        # positions
        r = logical_position[0]
        c = logical_position[1]
        #returning true if occupied
        occupied = True
        #returning false if the grid is empty
        if type == 'row' and self.row_status[c][r] == 0:
            occupied = False
        if type == 'col' and self.col_status[c][r] == 0:
            occupied = False

        return occupied
    # To update the board status
    def update_board(self, type, logical_position):
        r = logical_position[0]
        c = logical_position[1]
        val = 1
        if self.player1_turn:
            val =- 1
        # Giving -1 to the value if it is filled by player1 else 1 to the value
        if c < (number_of_dots-1) and r < (number_of_dots-1):
            self.board_status[c][r] += val

        if type == 'row':
            self.row_status[c][r] = 1
            if c >= 1:
                self.board_status[c-1][r] += val

        elif type == 'col':
            self.col_status[c][r] = 1
            if r >= 1:
                self.board_status[c][r-1] += val
        print(self.board_status, self.row_status, self.col_status)

    # To get the edge path
    def convert_grid_to_logical_position(self, grid_position):
        grid_position = np.array(grid_position)
        position = (grid_position-distance_between_dots/4)//(distance_between_dots/2)

        type = False
        #finding position and checking whethere there is a click in the colum edges or row edges.
        logical_position = []
        #cheching for row
        if position[1] % 2 == 0 and (position[0] - 1) % 2 == 0:
            r = int((position[0]-1)//2)
            c = int(position[1]//2) 
            logical_position = [r, c]
            type = 'row'
            # self.row_status[c][r]=1
        #checking for column
        elif position[0] % 2 == 0 and (position[1] - 1) % 2 == 0:
            c = int((position[1] - 1) // 2)
            r = int(position[0] // 2)
            logical_position = [r, c]
            type = 'col'
        print(logical_position,type)
        #returning positionvalues and whethere it is row or column
        return logical_position, type
    # To create or refresh the board with the player colour to the edges player click.
    def make_edge(self, type, logical_position):
        #finding startind and ending points.
        if type == 'row':
            start_x = distance_between_dots/2 + logical_position[0]*distance_between_dots
            end_x = start_x+distance_between_dots
            start_y = distance_between_dots/2 + logical_position[1]*distance_between_dots
            end_y = start_y
        elif type == 'col':
            start_y = distance_between_dots / 2 + logical_position[1] * distance_between_dots
            end_y = start_y + distance_between_dots
            start_x = distance_between_dots / 2 + logical_position[0] * distance_between_dots
            end_x = start_x
        #player1 colour
        if self.player1_turn:
            color = player1_color
        #player2 colour
        else:
            color = player2_color
        #filling edges with colour
        self.canvas.create_line(start_x, start_y, end_x, end_y, fill=color, width=edge_width)
    def refresh_board(self):
        #to place lines on canavas
        for i in range(number_of_dots):
            #horizontal lines
            x = i*distance_between_dots+distance_between_dots/2
            self.canvas.create_line(x, distance_between_dots/2, x,
                                    size_of_board-distance_between_dots/2,
                                    fill='gray', dash = (2, 2))
            #vertical lines
            self.canvas.create_line(distance_between_dots/2, x,
                                    size_of_board-distance_between_dots/2, x,
                                    fill='gray', dash=(2, 2))
        #to place dots
        for i in range(number_of_dots):
            for j in range(number_of_dots):
                start_x = i*distance_between_dots+distance_between_dots/2
                end_x = j*distance_between_dots+distance_between_dots/2
                self.canvas.create_oval(start_x-dot_width/2, end_x-dot_width/2, start_x+dot_width/2,
                                        end_x+dot_width/2, fill=dot_color,
                                        outline=dot_color)
    
    # To start the game
    def mainloop(self):
        self.window.mainloop()

game_instance = Dots_and_Boxes() 
game_instance.mainloop()