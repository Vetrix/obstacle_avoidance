#!/usr/bin/env python

'''
SELEKSI CALON KRU PROGRAMMING DAGOZILLA 2018
Take Home Test
File name: refactored_sudoku.py
Problem 2: Code Comprehension
'''

import sys
import numpy as np

# Bagian untuk membaca file eksternal, sesuai command line argument
def read_from_file(filename, table):
    with open(filename) as f:
        data = f.readlines()

    for i in range(9):
        for j in range(9):
            if data[i][j] == '-':
                table[i][j] = int(0)
            else:
                table[i][j] = int(data[i][j])

# Menampilkan tabel pada layar
def print_table(table):
    for i in range(9):
        for j in range(9):
            if table[i][j] == 0:
                print '-',
            else:
                print table[i][j],
        print('')
 
# Menyimpan tabel pada file eksternal
def save_table(filename, table):
    np.savetxt(filename, table, delimiter=' ', fmt='%i')


# Mencari bagian kosong pada tabel sudoku
def find_empty_location(table, l):
    for row in range(9):
        for col in range(9):
            if(table[row][col]==0):
                l[0]=row
                l[1]=col
                return True
    return False

# Melakukan cek angka pada baris
def used_in_row(table, row, num):
    for i in range(9):
        if(table[row][i] == num):
            return True
    return False

# Melakukan cek angka pada kolom
def used_in_col(table, col, num):
    for i in range(9):
        if(table[i][col] == num):
            return True
    return False

# melakukan cek angka pada blok 3x3
def used_in_block(table, row, col, num):
    for i in range(3):
        for j in range(3):
            if(table[i+row][j+col] == num):
                return True
    return False

# Cek sudoku keseluruhan
def is_valid(table, row, col, num):
    return not used_in_row(table, row, num) \
        and not used_in_col(table,col,num) \
        and not used_in_block(table,row - row%3,col - col%3,num)

def solve_sudoku(table):
     
    # 'l' is a list that stores rows and cols in find_empty_location Function
    l=[0,0]
    if(not find_empty_location(table, l)):
        return True

    # Assigning list values to row and col that we got from the above Function 
    row=l[0]
    col=l[1]

    # filling empty location with int 1 to 9
    for num in range(1,10):
        if is_valid(table, row, col, num):
            table[row][col]=num

            if solve_sudoku(table):
                return True
 
            # Else it fails, undo
            table[row][col] = 0
             
    # False mean sudoku have to backtrack
    return False


if __name__=="__main__":

    try:
        table = [[0 for i in range(9)] for j in range(9)]

        read_from_file(sys.argv[1], table)

        print "Your table:"
        print_table(table)          
        print "-----------------"

        if solve_sudoku(table):
            print "Solution:"
            print_table(table)
            save_table(sys.argv[2], table)
        else:
            print "No solution found"      
    except en(sys.argv) < 3:
        print "Error: ..."