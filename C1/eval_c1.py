import numpy as np
import time

class Game:
    def __init__(self, size=(8,8), seed=None, max_gen=10):
        # We use a predetermined seed to evaluate correct implementation
        if seed:
            np.random.seed(seed)         
        
        # Initialize the board with a random series of 1s and 0s
        self._board = np.random.randint(0,2,size)
        self._gen = 0
        self._max_gen = max_gen

    def neighbor_exists(self, board, row, col):   # returns true if neighbor exists, else fasle
        return board[row][col] == 1
	
    def count_neighbors(self, board, row, col):   # returns number of neighbors given a row and column
        num_neighbors = 0
        rows = len(board)
        cols = len(board[0])
		
        if row != 0:                # not on top row
            if self.neighbor_exists(board, row - 1, col):          # check space directly above
                num_neighbors += 1
            if col != 0:            # not in first col and top row
                if self.neighbor_exists(board, row - 1, col - 1):  # check top left diag
                    num_neighbors += 1
            if col != (cols - 1):   # not in last col and top row
                if self.neighbor_exists(board, row - 1, col + 1):  # check top right diag
                    num_neighbors += 1
				
        if row != (rows - 1):       # not in bot row
            if self.neighbor_exists(board, row + 1, col):          # check space directly below
                num_neighbors += 1
            if col != 0:            # not in first col and bot row
                if self.neighbor_exists(board, row + 1, col - 1):  # check bot left diag
                    num_neighbors += 1
            if col != (cols - 1):   # not in last col and top row
                if self.neighbor_exists(board, row + 1, col + 1):  # check bot right diag
                    num_neighbors += 1

        if col != 0:                # not on first col
            if self.neighbor_exists(board, row, col - 1):          # check space directly left
                num_neighbors += 1
				
        if col != (cols - 1):       # not on last col
            if self.neighbor_exists(board, row, col + 1):          # check space directly right
                num_neighbors += 1
        return num_neighbors
			
		
    def revive(self, board):  # returns list of cells to revive
        revive_list = []
        rows = len(board)
        cols = len(board[0])

        for i in range(rows):
            for j in range(cols):
                # revive dead cell if three neighbors exist
                if board[i][j] != 1 and self.count_neighbors(board, i, j) == 3:
                    revive_list.append((i, j))
        return revive_list
				

    def kill(self, board):    # returns list of cells to kill
        kill_list = []
        rows = len(board)
        cols = len(board[0])
		
        for i in range(rows):
            for j in range(cols):
                num_neighbors = self.count_neighbors(board, i, j)
		# if neighbors != 2 or 3, die
                if board[i][j] == 1 and (num_neighbors != 2 or num_neighbors != 3):
                    kill_list.append((i, j))
        return kill_list

    def update_board(self, board, k_list, r_list):    # updates the board according to the lists
        if len(k_list) != 0:
            for cell in k_list:
                board[cell[0]][cell[1]] = 0
        if len(r_list) != 0:
            for cell in r_list:
                board[cell[0]][cell[1]] = 1

        return board

    def update(self):
        board = np.copy(self._board)
        #print(board)   # the copy function seems to create an empty 2D array
        ''' Insert your code for updating the board based on the rules below '''
        board = self.update_board(board, self.kill(board), self.revive(board))
        
        self._board = board
        
    def play(self, delay=.1):
        while self._gen < self._max_gen:
            # Start the generation by drawing the current board
            self.draw()
            
            # Next we update each of the cells according to the rules 
            self.update()

            # Increment the generation and sleep to make the visualization easier
            self._gen += 1
            time.sleep(delay)

    def time_run(self, gens=1000):
        start = time.time()
        for _ in range(gens):
            self.update()
        print(f'Average update time: {(time.time()-start)/gens*1000} ms')

    def draw(self):
        for row in self._board:   
            # Print a full block for each alive cell and an empty one for dead cells bounded by |
            print('|'.join(['▇' if c else ' ' for c in row]))

        print(f'Generation: {self._gen}')


if __name__ == "__main__":
    # If this file is run directly from the command line, run the game
    g = Game()
    g.time_run()
    g.play()  # Uncomment this to see the generational progression
