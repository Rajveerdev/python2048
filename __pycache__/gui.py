from game import Board2048
from tkinter import Tk, Label, Frame, Event

BACKGROUND_COLOR = "#f0ffff"
TILE2_COLOUR =  "#26235b"
TILE4_COLOUR = "#812878"
TILE8_COLOUR = "#a22160"
TILE16_COLOUR = "#cc2336"
TILE32_COLOUR = "#e4682a"
TILE64_COLOUR = "#f69824"
TILE128_COLOUR = "#e84d3d"
TILE256_COLOUR = "#fdc72e"
TILE512_COLOUR = "#e09b00"
TILE1024_COLOUR = "#bc473a" 
TILE2048_COLOUR = "#1d3a45"
TILE4096_COLOUR = "#3eb049"
TILE8192_COLOUR = "#602c50"
FOREGROUND_COLOR = "#111111"

class GUIViewer:
    '''Present a graphical interface for 2048 to users.
    Use left, right, up, and down keyboard keys for movement.'''
    
    def __init__(self, board: Board2048):
        '''Open a window with a Board2048 board.'''
        
        self.board = board
        self.size = board.get_size()
        self.init_window()
        self.init_board()
        self.update_view()
        self.window.mainloop()
        


    def key(self, k: Event):
        '''React to a keypress event k.'''
        
        curr_key = k.keysym
        
        if curr_key == "Left":
            self.board.left()
        elif curr_key == "Right":
            self.board.right()
        elif curr_key == "Up":
            self.board.up()
        elif curr_key == "Down":
            self.board.down()    
        self.update_view()
        
        
    def init_window(self):
        '''Initialize main window.'''
        
        self.window = Tk()
        self.window.title("Score: {}".format(self.board.get_score()))
        self.window.resizable(height=0, width=0)
        self.window.geometry("600x600+0+0")
        self.window.bind("<Key>", self.key)
        self.font = ("Courier", 160 // self.size, "bold")
        self.labels = []
        
        
    def init_label(self, i, j):
        '''Initialize label at row i, column j, of window.'''
        
        frm1 = Frame(self.window,bg="grey")
        frm1.grid(row=i,column=j, sticky="NESW", padx=4, pady=4)
        frm1.grid_rowconfigure(0, weight=1)
        frm1.grid_columnconfigure(0, weight=1)
        label = Label(frm1, bg="#9e948a", width=5, font=self.font, text = "")
        label.grid(padx=0, pady=0)
        label.master.configure(bg="#9e948a")
        return label


    def init_board(self):
        '''Initialize all labels and store labels in self.labels'''
        
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(self.init_label(i, j))
                self.window.grid_rowconfigure(i, weight=1)
                self.window.grid_columnconfigure(j, weight=1)
            self.labels.append(row)


    def update_view(self):
        '''Update view contents based on changing model state.'''
        
        self.window.title("Score: {}".format(self.board.get_score()))
        # label_score = Label(self.window, font=self.font, text = "Score: " + str(self.board.get_score()))
        
        for i in range(self.size):
            for j in range(self.size):
                currval = self.board.get_cell(i, j)
                self.tile_colour(i, j, currval)
                
        if self.board.game_over():
            print("Game Over!")
            
        

    def tile_colour(self, i, j, currval):
        if(currval == 2):
            self.labels[i][j].configure(text=str(currval),
                                        bg=TILE2_COLOUR, fg=FOREGROUND_COLOR)
            self.labels[i][j].master.configure(bg=TILE2_COLOUR)
        elif(currval == 4):
            self.labels[i][j].configure(text=str(currval),
                                        bg=TILE4_COLOUR, fg=FOREGROUND_COLOR)
            self.labels[i][j].master.configure(bg=TILE4_COLOUR)
        elif(currval == 8):
            self.labels[i][j].configure(text=str(currval),
                                        bg=TILE8_COLOUR, fg=FOREGROUND_COLOR)
            self.labels[i][j].master.configure(bg=TILE8_COLOUR)
        elif(currval == 16):
            self.labels[i][j].configure(text=str(currval),
                                        bg=TILE16_COLOUR, fg=FOREGROUND_COLOR)
            self.labels[i][j].master.configure(bg=TILE16_COLOUR)
        elif(currval == 32):
            self.labels[i][j].configure(text=str(currval),
                                        bg=TILE32_COLOUR, fg=FOREGROUND_COLOR)
            self.labels[i][j].master.configure(bg=TILE32_COLOUR)
        elif(currval == 64):
            self.labels[i][j].configure(text=str(currval),
                                        bg=TILE64_COLOUR, fg=FOREGROUND_COLOR)
            self.labels[i][j].master.configure(bg=TILE64_COLOUR)
        elif(currval == 128):
            self.labels[i][j].configure(text=str(currval),
                                        bg=TILE128_COLOUR, fg=FOREGROUND_COLOR)
            self.labels[i][j].master.configure(bg=TILE128_COLOUR)
        elif(currval == 256):
            self.labels[i][j].configure(text=str(currval),
                                        bg=TILE256_COLOUR, fg=FOREGROUND_COLOR)
            self.labels[i][j].master.configure(bg=TILE256_COLOUR)
        elif(currval == 512):
            self.labels[i][j].configure(text=str(currval),
                                        bg=TILE512_COLOUR, fg=FOREGROUND_COLOR)
            self.labels[i][j].master.configure(bg=TILE512_COLOUR)
        elif(currval == 1024):
            self.labels[i][j].configure(text=str(currval),
                                        bg=TILE1024_COLOUR, fg=FOREGROUND_COLOR)
            self.labels[i][j].master.configure(bg=TILE1024_COLOUR)
        elif(currval == 2048):
            self.labels[i][j].configure(text=str(currval),
                                        bg=TILE2048_COLOUR, fg=FOREGROUND_COLOR)
            self.labels[i][j].master.configure(bg=TILE2048_COLOUR)
        elif(currval == 4096):
            self.labels[i][j].configure(text=str(currval),
                                        bg=TILE4096_COLOUR, fg=FOREGROUND_COLOR)
            self.labels[i][j].master.configure(bg=TILE4096_COLOUR)
        elif(currval == 8192):
            self.labels[i][j].configure(text=str(currval),
                                        bg=TILE8192_COLOUR, fg=FOREGROUND_COLOR)
            self.labels[i][j].master.configure(bg=TILE8192_COLOUR)
        else:
            self.labels[i][j].configure(text="",
                                        bg=BACKGROUND_COLOR, fg=FOREGROUND_COLOR)
            self.labels[i][j].master.configure(bg=BACKGROUND_COLOR)
            
    def dis_score(self):
        return( Label(self.window,
                            text=str(self.board.get_score())))


if __name__ == "__main__":
    b = Board2048(4)
    
    # Uncomment to test a particular matrix state
    b.set_matrix([
        [0,2,2,0],
        [0,2,0,2],
        [2,2,0,0],
        [2,0,0,2]
        ])
    
    GUIViewer(b)    