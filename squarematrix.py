class SquareMatrix:
    '''This class is complete.'''
    
    def __init__(self, size: int):
        '''Create new size x size SquareMatrix object.'''
        
        self._matrix = self._blank_matrix(size)
        self._size = size
        
        
    def _blank_matrix(self, size: int) -> list:
        '''Return a size x size list of lists containing zeroes'''
        
        board = []
        for _ in range(size):
            row = [0] * size
            board.append(row)
        return board
    
    
    def get_size(self) -> int:
        '''Return the length (or width) of the SquareMatrix'''
        
        return self._size
    
    
    def get_cell(self, x: int, y: int) -> object:
        '''Return the contents of cell at row x and column y'''
        
        return self._matrix[x][y]
    
    
    def set_cell(self, x: int, y: int, v: object) -> None:
        '''Set the value of cell at row x and column y to v.'''
        
        self._matrix[x][y] = v
        
    
    def set_matrix(self, m: list) -> None:
        '''Iff m is a matrix the same size as self,
        replace the contents of self with the contents of m.'''
        
        if len(m) == self._size and len(m[0]) == self._size:
            self._matrix = m
            
            
    def __contains__(self, i: object) -> bool:
        '''Return True iff i is an internal cell in self.'''

        for row in self._matrix:
            if i in row:
                return True
        return False


    def flip(self):
        '''Reverse all rows in self and return self.'''
        
        for row in self._matrix:
            row.reverse()
        return self
        
        
    def transpose(self):
        '''Turn self's rows into columns and columns into rows. Return self.'''
        
        after_board = self._blank_matrix(self._size)
        for i in range(self._size):
            for j in range(self._size):
                after_board[j][i] = self._matrix[i][j]
        self._matrix = after_board
        return self


    def rotate(self):
        '''Rotate self clockwise and return self.'''
        
        self.transpose()
        self.flip()
        return self


    def unrotate(self):
        '''Rotate self counter-clockwise and return self.'''
        
        self.flip()
        self.transpose()
        return self
    

        
        
    def __str__(self) -> str:
        '''Return the string representation of self.'''
        
        s = ""
        for row in self._matrix:
            s+= str(row)
            s+='\n'
        return s