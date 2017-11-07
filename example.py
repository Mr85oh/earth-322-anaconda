#!/usr/bin/env python

def calculate_squares(num):
    squares = []
    import pdb
    pdb.set_trace()
    for i in range(num):
        i_squared = i**2
        squares.append(i_squared)
    return squares

def main():
    ten_squares = calculate_squares(10)
    print(ten_squares)

if __name__ == '__main__':
    main()