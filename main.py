"""
this is maze problem imp
authors: hooman mesalazar (974407) - parham afsharnia (974409)

"""
from Search_Algorithms import Algorithms
import time

f_name = 'maze2.txt'
a = Algorithms(f_name)

print('running BFS:')
t1 = time.time()
print('reach target? ', a.BFS())
exetime = time.time() - t1
print('execution time:', exetime)
print('----------------------')

a.maze.flush_visited()
a.maze.flush_parents()

print('running DFS:')
t1 = time.time()
print('reach target? ', a.DFS())
exetime = time.time() - t1
print('execution time:', exetime)
print('----------------------')

a.maze.flush_visited()
a.maze.flush_parents()

print('running IDS:')
t1 = time.time()
print('reach target? ', a.IDS())
exetime = time.time() - t1
print('execution time:', exetime)
