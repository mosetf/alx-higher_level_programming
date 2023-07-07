#!/usr/bin/python3 

 import sys 
  
  
 if len(sys.argv) != 2: 
     print("Usage: nqueens N") 
     exit(1) 
 try: 
     N = sys.argv[1] 
     N = int(N) 
 except ValueError: 
     print("N must be a number") 
     exit(1) 
  
 if N < 4: 
     print("N must be at least 4") 
     exit(1) 
  
  
 def generate_matrix(N): 
     """ 
     Generates a square matrix with dots
  
     Args: 
         N (int): size of square matrix 
  
     Returns: 
         list: A square matrix with dimensions `size x size` 
         Mad of dots
     """ 
     board = [["." for row in range(N)] for column in range(N)] 
     return board 
  
  
 def create_list(board, N): 
     """ 
     Creates a List from the Matrix 
  
     Args: 
         board: Matrix 
         N: number
  
     Returns: 
         list: list of positions 
     """ 
     matrix = [] 
     for row in range(N): 
         for column in range(N): 
             if board[row][column] == "X": 
                 matrix.append([row, column]) 
     return matrix 
  
  
 def add_to_results(board, rl, N): 
     """ 
     Plays with the solution to achieve the results
  
     Args: 
         board (list): board 
         rl (list): list of results 
         N (int): N 
     """ 
     temp = [] 
     for row in range(N): 
         string = "" 
         for column in range(N): 
             string += board[row][column] 
         temp.append(string) 
     rl.append(temp) 
  
  
 def is_safe(row, column, board, N): 
     """ 
     Checks authenticity of addition
  
     Args: 
         row (int): row 
         column (int): column 
         board (list): board 
         N (int): N 
  
     Returns: 
         bool: True if safe False if not 
     """ 
     x = row 
     y = column 
  
     while x >= 0: 
         if board[x][y] == "X": 
             return False 
         else: 
             x -= 1 
  
     x = row 
     y = column 
     while (y < N and x >= 0): 
         if board[x][y] == "X": 
             return False 
         else: 
             y += 1 
             x -= 1 
  
     x = row 
     y = column 
     while (y >= 0 and x >= 0): 
         if board[x][y] == "X": 
             return False 
         else: 
             x -= 1 
             y -= 1 
     return True 
    
 def NQueens(row, rl, board, N): 
     """ 
     Recursive function to solve NQueens 
     Args: 
         row (int): row 
         rl (list): results_list 
         board (list): board 
         N (int): N 
     """ 
     if row == N: 
         add_to_results(board, rl, N) 
         return 
  
     for column in range(N): 
         if is_safe(row, column, board, N): 
             board[row][column] = "X" 
             NQueens(row + 1, rl, board, N) 
             board[row][column] = "." 
  
  
 if __name__ == "__main__": 
  
     board=generate_matrix(N) 
  
     rl= [] 
     NQueens(0, results_list, board, N) 
  
     if len(rl) != 0: 
         for result in rl: 
             print(create_list(result, N))
