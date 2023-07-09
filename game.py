from random import randint
from squarematrix import SquareMatrix
   
        
class Board2048(SquareMatrix):
    '''This class represents a specific kind of SquareMatrix: a game board
    for the game 2048. Represent blank tiles as 0.
    '''

    ## Initializing the board

    def __init__(self, size: int):
        '''Create a new size x size Board2048, seed the initial score,
        and create the initial game state.
        This method is complete.'''

        self._score = 0
        super().__init__(size)
        self._new_game()
        self._game_over_bool = False

    def _new_game(self) -> None:
        '''Spawn initial board state: Two 2-tiles in random locations.
        This method is complete.
        '''
        
        self._spawn_random(2)
        self._spawn_random(2)


    def _board_full(self) -> bool:
        '''Return True iff there are no blank tiles on the board.
        This method is complete.'''
        
        return not (0 in self)


    def _spawn_random(self, value: int):
        '''Spawn a tile with value in a random unoccupied location.
        If there are no blank spaces on the board, do nothing.'''
        
        
        if (not(self._board_full())):
            r = randint(0, self.get_size()-1)
            c = randint(0, self.get_size()-1)
            
            while (self.get_cell(r,c) != 0):
                
                r = randint(0, self.get_size()-1)
                c = randint(0, self.get_size()-1)
                
            self.set_cell(r, c, value) 
            
        else :
            print("Cannot add another tile")
    

# Manipulate game state

    def _shift(self):
        '''Move all non-blank tiles in self to the beginning of their row.
        Return True iff any changes resulted from the operation.
        Example:
        [0, 2, 0, 4] -> [2, 4, 0, 0]
        Do not merge neighbours:
        [0, 2, 0, 2] -> [2, 2, 0, 0], not [4, 0, 0, 0]
        '''
        
        for row in self._matrix:
            for i in range(len(row)):
                
                if (row[i] != 0):
                    j = -1
                    
                    while (i+j >= 0):
                        
                        if(row[i+j] == 0):
                            
                            row[i+j] = row[i+j+1]
                            row[i+j+1] = 0
                            
                        else:
                            break
                        
                        j -= 1
        
    
    def _merge(self) -> bool:
        '''Merge pairs of neighbouring tiles that match in value, from left to right.
        Increment score with the values of all newly merged tiles.
        Return True iff any changes resulted from the operation.
        
        Replace the merged tile with a blank tile.
        Do not move unmerged tiles.
        Do not shift tiles to cover blank lines.
        Example: [0, 2, 2, 8] -> [0, 4, 0, 8]
        
        Only use each tile once, i.e., do not chain merges:
        Example: [4, 2, 2, 0] -> [4, 4, 0, 0], not [8, 0, 0, 0]
        
        If multiple tiles can be merged, merge the ones closest to the beginning of the row.
        Example: [2, 2, 2, 0] -> [4, 0, 2, 0], not [2, 4, 0, 0]
        
        If more than one pair of tiles can be merged, merge all pairs:
        Example: [2, 2, 2, 2] -> [4, 0, 4, 0]
        '''
        
        for row in self._matrix:
            for i in range(len(row)):
                
                if (row[i] != 0 and i+1 < len(row)):
                    if (row[i] == row[i+1]):
                        row[i] += row[i+1]
                        self._score += row[i]
                        row[i+1] = 0

                    
                

          
    def _shift_merge(self):
        '''Shift and merge tiles to complete a "left" equivalent move.
        Return True iff any changes resulted from this operation.
        '''
        temp_m = self._blank_matrix(self.get_size())
        
        for i in range(self.get_size()):
            for j in range(self.get_size()):
                temp_m[i][j] = self.get_cell(i, j)
        
        self._shift()
        self._merge()
        self._shift()
        
        for i in range(self.get_size()):
            for j in range(self.get_size()):
                if (self.get_cell(i, j) != temp_m[i][j]):
                    # The game_over_bool means that the conditions for a game over have not been partially met 
                    self._game_over_bool = False
                    # The cells of the matrix before and after the shift merge are different meaning another tile can spawn
                    return True
        # The game_over_bool means that the conditions for a game over have been partially met
        self._game_over_bool = True
        # The cells are all the same meaning no change and no spawning the new tile
        return False       
    

    def left(self):
        '''Move left in the game.
        This method is complete.
        '''

        self._update(self._shift_merge())
        


    def right(self):
        '''Move right in the game.'''
        self.flip()
        self._update(self._shift_merge())
        self.flip()


    def down(self):
        '''Move down in the game.'''
        
        self.rotate()
        self._update(self._shift_merge())
        self.unrotate()
        
        
    def up(self):
        '''Move up in the game.'''
        
        self.unrotate()
        self._update(self._shift_merge())
        self.rotate()
 

    # Update the board after a move



    def _update(self, change: bool):
        '''If the board has changed after a move, spawn the next tile.
        '''
        if (change == True):
            self._spawn_next()
            
        
 
 
    def _spawn_next(self) -> None:
        '''Spawn the next tile for the game in a random location.
        - 90% chance: 2-tile
        - 10% chance: 4-tile
        '''
        
        rand_chance = randint(0, 9)
        
        if (0 <= rand_chance < 9):
            self._spawn_random(2)
        else:
            self._spawn_random(4)



    # Scoring, winning, and losing

    def get_score(self) -> int:
        '''Return the current score.
        This method is complete.'''
        
        return self._score
    
    
    def win(self) -> bool:
        '''Return True iff the victory condition for 2048 has been reached.
        This method is complete.'''
        
        return 2048 in self


    def game_over(self) -> bool:
        '''Return True iff the board is full and there are no possible
        merges possible.'''
        
        if (self._game_over_bool == True):
            self.counter = 0
            for i in range(self.get_size()):
                for j in range(self.get_size()):
                    if (self.get_cell(i, j)):
                        self.counter += 1
                        # print("Counter: " + str(self.counter) + " i: " + str(i) + " j: " + str(j))
            if (self.counter == (self.get_size() * self.get_size())):
                return True
            else:
                return False
        return False
                    




class TextViewer:
    '''Present a text-based interface for 2048 to users.
    Use keys WASD for up, left, down, and right. Use Q to quit.
    This class is complete. '''
    
    def __init__(self, board: Board2048):
        '''Begin endless input loop with Board2048 board.'''
        
        self.board = board # squarematrix
        while True:
            print(self.board)
            print("Score: {}".format(self.board.get_score()))
            if self.board.game_over():
                print("Game Over!")
                break
            command = input("WASD or Quit: ").lower()
            if command == 'q':
                break
            elif command == "w":
                self.board.up()
            elif command == "s":
                self.board.down()
            elif command == "a":
                self.board.left()
            elif command == "d":
                self.board.right()
            else:
                print("Huh?")




if __name__ == "__main__":
    
    # Create a new test board
    b = Board2048(4)
    
    # Uncomment this to set the initial state of the matrix for test purposes
    '''
    b.set_matrix([
        [0,2,2,0],
        [0,2,0,2],
        [2,2,0,0],
        [2,0,0,2]
        ])
    '''
    
    b.set_matrix([
        [0,0,4,2],
        [0,4,2,0],
        [0,2,0,2],
        [2,0,2,0]
        ])
    
    # print(b)

    # Example test call:
    #b.left()
    #print(b)

    # Uncomment this to play the game using the text viewer:
    TextViewer(b)