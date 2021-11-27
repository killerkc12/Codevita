'''
Constellation
Three characters { #, *, . } represents a constellation of stars and galaxies in space. Each galaxy is demarcated by # characters. There can be one or many stars in a given galaxy. Stars can only be in the shape of vowels { A, E, I, O, U }. A collection of * in the shape of the vowels is a star. A star is contained in a 3x3 block. Stars cannot be overlapping. The dot(.) character denotes empty space.
Given 3xN matrix comprising of { #, *, . } character, find the galaxy and stars within them.
Note: Please pay attention to how vowel A is denoted in a 3x3 block in the examples section below.

Constraints
3 <= N <= 10^5
Input
Input consists of a single integer N denoting the number of columns.
Output
The output contains vowels (stars) in order of their occurrence within the given galaxy. The galaxy itself is represented by the # character.

Example 1
Input
18
* . * # * * * # * * * # * * * . * .
* . * # * . * # . * . # * * * * * *
* * * # * * * # * * * # * * * * . *
Output
U#O#I#EA
Explanation
As it can be seen that the stars make the image of the alphabets U, O, I, E, and A respectively.

Example 2
Input
12
* . * # . * * * # . * .
* . * # . . * . # * * *
* * * # . * * * # * . *
Output
U#I#A
Explanation
As it can be seen that the stars make the image of the alphabet U, I, and A.

Possible solution:
Input:
12
* . * # . * * * # . * .
* . * # . . * . # * * *
* * * # . * * * # * . *

'''



# def find(ch, length):
#     print('fi')
#     print(length)


# # startinng of the program
# ch = [
#         ['*', '.', '*', '#', '.', '*', '*', '*', '#', '.', '*', '.'],
#         ['*', '.', '*', '#', '.', '.', '*', '.', '#', '*', '*', '*'],
#         ['*', '*', '*', '#', '.', '*', '*', '*', '#', '*', '.', '*']
# ]

from collections import deque
def initialize():
    q = deque()
    # A
    s = ""
    q.append(['.', '*', '*'])
    q.append(['*', '*', '.'])
    q.append(['.', '*', '*'])
    s = ''.join(map(str, q))
    vowels[s] = 'A'
    q.clear()
    #E
    q.append(['*', '*', '*'])
    q.append(['*', '*', '*'])
    q.append(['*', '*', '*'])
    s = ''.join(map(str, q))
    vowels[s] = 'E'
    q.clear()
    
    #I
    q.append(['*', '.', '*'])
    q.append(['*', '*', '*'])
    q.append(['*', '.', '*'])
    s = ''.join(map(str, q))
    vowels[s] = 'I'
    q.clear()
    #O
    q.append(['*', '*', '*'])
    q.append(['*', '.', '*'])
    q.append(['*', '*', '*'])
    s = ''.join(map(str, q))
    vowels[s] = 'O'
    q.clear()
    #U
    q.append(['*', '*', '*'])
    q.append(['.', '.', '*'])
    q.append(['*', '*', '*'])
    s = ''.join(map(str, q))
    vowels[s] = 'U'
    q.clear()
    return vowels
vowels = {}
vowels = initialize()
n = int(input())
x = []
for i in range(n):
    x.append(['.', '.', '.'])
for i in range(3):
    l = []
    l = list(input())
    for j in range(n):
        x[j][i] = l[j]
    
constellation = ""
star = deque()
for i in range(n):
    if len(star) ==3:
        s = ''.join(map(str, star))
        if s in vowels:
            constellation += vowels[s]
            star.clear()
        else:
            star.popleft()
    if x[i]==['#', '#', '#']: 
        star.clear()
        constellation += '#'
        continue
    star.append(x[i])
if len(star)==3:
    s = ''.join(map(str, star))
    if s in vowels:
        constellation += vowels[s]
        
print(constellation, end="")