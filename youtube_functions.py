import time
from flask import session

YOUTUBEKEYBOARD = [[ 'A', 'B', 'C', 'D', 'E', 'F', 'G' ],
                   [ 'H', 'I', 'J', 'K', 'L', 'M', 'N'],
                   [ 'O', 'P', 'Q', 'R', 'S', 'T', 'U'],
                   [ 'V', 'W', 'X', 'Y', 'Z', '-', '\'' ]]

def get_key_coords(key):
    kb = YOUTUBEKEYBOARD

    for row in kb:
        for row_key in row:
            if row_key == key:
                column = row_key
                return kb.index(row), row.index(column)

def get_key_directions(currentKey, newKey):
    directions = []
    horizontal_direction = get_key_coords(newKey)[1] - get_key_coords(currentKey)[1]
    vertical_direction = get_key_coords(newKey)[0] - get_key_coords(currentKey)[0]

    if horizontal_direction > 0:
        for i in range(abs(horizontal_direction)):
            directions.append('right')
    if horizontal_direction < 0:
        for i in range(abs(horizontal_direction)):
            directions.append('left')

    if vertical_direction > 0:
        for i in range(abs(vertical_direction)):
            directions.append('down')
    if vertical_direction < 0:
        for i in range(abs(vertical_direction)):
            directions.append('up')

    return directions

def input_keys(roku, keylist, new_key):
    for key in keylist:
        if key == 'left':
            roku.left()
        if key == 'right':
            roku.right()
        if key == 'up':
            roku.up()
        if key == 'down':
            roku.down()
        time.sleep(.1)
    roku.select()
    session['LastKey'] = new_key
    return


def youtube_search_cursor(roku):
    roku.left()
    roku.up()
    roku.right()
    roku.right()