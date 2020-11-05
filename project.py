from tkinter import *


size_of_board = 400
number_of_dots = 4
distance_between_dots = size_of_board / (number_of_dots)
dot_width = 0.25*size_of_board/number_of_dots
dot_color = '#0492CF'


class Dots_and_Boxes():

    # Initialization functions
    def __init__(self):
        self.window = Tk()
        self.window.title('Dots_and_Boxes')
        self.canvas = Canvas(self.window, width=size_of_board, height=size_of_board)
        self.canvas.pack()
        self.refresh_board()
    def refresh_board(self):
        for i in range(number_of_dots):
            #to display lines 
            x = i*distance_between_dots+distance_between_dots/2
            #horizontal lines in canvas
            self.canvas.create_line(x, distance_between_dots/2, x,
                                    size_of_board-distance_between_dots/2,
                                    fill='gray', dash = (2, 2))
            #vertical lines in canvas
            self.canvas.create_line(distance_between_dots/2, x,
                                    size_of_board-distance_between_dots/2, x,
                                    fill='gray', dash=(2, 2))
        # code display dots
        for i in range(number_of_dots):
            for j in range(number_of_dots):
                start_x = i*distance_between_dots+distance_between_dots/2 #start point
                end_x = j*distance_between_dots+distance_between_dots/2 #end point
                #dot placement
                self.canvas.create_oval(start_x-dot_width/2, end_x-dot_width/2, start_x+dot_width/2,
                                        end_x+dot_width/2, fill=dot_color,
                                        outline=dot_color)


    # To start the game
    def mainloop(self):
        self.window.mainloop()

game_instance = Dots_and_Boxes()
game_instance.mainloop()