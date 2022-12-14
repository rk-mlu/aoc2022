""" Advent of Code 2022 -- Day 08 -- """

import aoc
import numpy as np

def parse_input(data):
    lines = data.splitlines()

    num_row = len(lines)
    num_col = len(lines[0])
    dim = num_row, num_col

    mat = np.zeros((num_row, num_col), dtype=np.int32)

    for n, line in enumerate(lines):
        for m, c in enumerate(line):
            mat[n,m] = int(c)

    return mat, dim

def check_vis(M, i, j):
    maxval = np.zeros(4)
    maxval[0] = np.amax(M[i, :j])
    maxval[1] = np.amax(M[i, j+1:])
    maxval[2] = np.amax(M[:i, j])
    maxval[3] = np.amax(M[i+1:, j])
    
    for k in range(4):
        if maxval[k] < M[i, j]:
            return 1

    return 0


def num_visible_trees(M, dim):
    count = 2*(dim[0] + dim[1]-2)

    for i in range(1, dim[0]-1):
        for j in range(1, dim[1]-1):
            count += check_vis(M, i, j) 

    return count

def scenic_tree(M, dim, i, j):

    h = M[i,j]

    su = i 
    for l in range(i):
        if M[i-l-1,j] >= h:
            su = l +1
            break

    sd = dim[0] - i - 1
    for r in range(dim[0]-i-1):
        if M[i+r+1,j] >= h:
            sd = r + 1
            break

    sl = j 
    for l in range(j):
        if M[i,j-l-1] >= h:
            sl = l + 1
            break

    sr = dim[1] - j - 1
    for r in range(dim[1]-j-1):
        if M[i,j+1+r] >= h:
            sr = r + 1
            break
    # print(su, sl, sd, sr)
    return sl*sr*sd*su

def scenic_score(M, dim):

    score = np.zeros_like(M)

    for i in range(1, dim[0]-1):
        for j in range(1, dim[1]-1):
            score[i,j] = scenic_tree(M, dim, i, j)
    print(score)

    return np.amax(score)




if __name__ == '__main__':
    data = aoc.get_input('input.txt')
    M, dim = parse_input(data)
    c = num_visible_trees(M, dim)
    print(f'Part I: {c} trees')

    high = scenic_score(M, dim)
    print(f'Part II: highest scenic score is {high}')

    # print(scenic_tree(M, dim, 3, 2))

