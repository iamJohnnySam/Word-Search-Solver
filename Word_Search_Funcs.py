from pickle import TRUE
import enchant
dictionary = enchant.Dict("en_GB")

def getWord(grid, row, col, rows, cols):

    #Iterate left to right
    search = ""
    for i in range (cols - col):
        search = search+grid[row][col+i]
    searchWord(search, row, col, '\u2192')

    #Iterate top to bottom
    search = ""
    for i in range (rows - row):
        search = search+grid[row+i][col]
    searchWord(search, row, col, '\u2193')

    #Iterate top left to bottom right
    search = ""
    for i in range (min((cols - col),(rows - row))):
        search = search+grid[row+i][col+i]
    searchWord(search, row, col, '\u2198')


def searchWord (word, row, col, direc):
    for i in range(len(word)):
        f = checkDict(word[0:i])
        if f:
            print(row, col, direc, word[0:i])

def checkDict (word):
    if (len(word)>2):
        found = dictionary.check(word)
        if found:
            return(True)
    return(False)