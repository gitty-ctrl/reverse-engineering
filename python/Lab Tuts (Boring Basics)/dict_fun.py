import pprint 
"""spam = {'name': 'Jander', 'age': 100}

x = 'name' in spam.keys()

y = 'Jander' in spam.values()"""

#print(f"\n {x} \n {y}")

"""msg = "It was a birght cold day in April, and the clocks were strinking thirteen."
count = {}


for char in msg:
    count.setdefault(char, 0)
    count[char] = count[char] + 1

pprint.pprint(count)"""

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
 print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
 print('-+-+-')
 print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
 print('-+-+-')
 print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print(f"Turn for {turn}. Move on which space?")
    move = input()
    theBoard[move] = turn
    if turn == 'X':
       turn = '0'
    else:
       turn = 'X'
print(theBoard)