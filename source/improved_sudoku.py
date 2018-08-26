#!/usr/bin/env python

'''
SELEKSI CALON KRU PROGRAMMING DAGOZILLA 2018
Take Home Test
File name: improved_sudoku.py
Problem 2: Code Comprehension
'''

import sys
import numpy as np
import cProfile

def read_from_file(filename, board):
    with open(filename) as f:
        data = f.readlines()

    for i in range(9):
        for j in range(9):
            if data[i][j] == '-':
                board[i][j] = int(0)
            else:
                board[i][j] = int(data[i][j])


# What does this function do?
# This function prints what's in table board[i][j], to the screen.
def print_board(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                print '-',
            else:
                print board[i][j],
        print('')
 

def save_board(filename, board):
    np.savetxt(filename, board, delimiter=' ', fmt='%i')


# What does this function do?
# Find int 0 in the board, and returning boolean value
def find_empty_location(board, l):
    for row in range(9):
        for col in range(9):
            # What happens inside the 'if' section?
            # Cheking the board[row][col] is 0, if it is, returns value True
            if(board[row][col]==0):
                l[0]=row
                l[1]=col
                return True
    return False
    # Why does this function return a boolean value?
    # Because it will be used as a condition in conditional statement


def used_in_row(board, row, num):
    for i in range(9):
        if(board[row][i] == num):
            return True
    return False


def used_in_col(board, col, num):
    for i in range(9):
        if(board[i][col] == num):
            return True
    return False


def used_in_block(board, row, col, num):
    for i in range(3):
        for j in range(3):
            if(board[i+row][j+col] == num):
                return True
    return False


def is_valid(board, row, col, num):
    return not used_in_row(board, row, num) \
        and not used_in_col(board,col,num) \
        and not used_in_block(board,row - row%3,col - col%3,num)
    # What makes this function return True (what makes it valid for a number in a given location)?
    # It will returns True if the sudoku solved with valid answers
    # all in a row consist of 1 to 9, all of in a col cons. 1 to 9, and all of in 3x3 box const. of 1 to 9


# Explain the algorithm in this function!
# Initialize l as [0,0], then find form empty location, then start filling it with numbers, backtracking until sudoku valid.
def solve_sudoku(board):
     
    # 'l' is a list that stores rows and cols in find_empty_location Function
    l=[0,0]
     
    # What does this 'if' block check?
    # check is there any empty location on the board, if it is, then proceed
    # What will happen if the program enters the following 'if' block?
    # It will check for int 0, and return
    if(not find_empty_location(board, l)):
        # In what way does this True value affect the program?
        # If theres no empty location, it's finished
        return True

    # Assigning list values to row and col that we got from the above Function 
    row=l[0]
    col=l[1]

    # What does this block do?
    # filling empty location with int 1 to 9
    for num in range(1,10):
        if is_valid(board, row, col, num):
            board[row][col]=num

            # What does this 'if' section check?
            # return if the board completed
            if solve_sudoku(board):
                return True
 
            # Else it fails, undo
            board[row][col] = 0
             
    # What is this False value for? Will this function always return False?
    # False mean sudoku have to backtrack
    return False


# Driver main function to test above functions
if __name__=="__main__":
    # What is this 'if' for?
    # Check the module name,and checking errors
    # Is there any other way to check and handle error like this without using 'if else'?
    # Using exceptions
    # What does the value of len(sys.argv) represent?
    # Number of command line arguments
    try:
       	board = [[0 for i in range(9)] for j in range(9)]

        # What is sys.argv[1]?
        # List created from command line argument
       	read_from_file(sys.argv[1], board)

       	print "Your board:"
       	print_board(board)        	
       	print "-----------------"

       	if solve_sudoku(board):
           	print "Solution:"
           	print_board(board)
           	save_board(sys.argv[2], board)
       	else:
           	print "No solution found"      
    except en(sys.argv) < 3:
       	print "Error: ..."
