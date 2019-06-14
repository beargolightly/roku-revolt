import time
from flask_wtf import FlaskForm
from wtforms import StringField

SPECIAL_CHARACTERS = ' '

class YouTubeKeyBoardForm(FlaskForm):
    sendkeys = StringField('Text to send to Youtube app:')

class YouTubeKeyboardController:

    def __init__(self, roku, currentKey):

        self.roku = roku
        self.YOUTUBEKEYBOARD = [['A','B','C','D','E','F','G' ],
                                ['H','I','J','K','L','M','N'],
                                ['O','P','Q','R','S','T','U'],
                                ['V','W','X','Y','Z','-','\'']]

        self.currentKey = currentKey

    def type_phrase(self, phrase, delay):

        complete_button_list = []

        for letter in phrase:
            newKey = letter
            button_list = self._get_button_list(self.currentKey, newKey)
            complete_button_list += button_list
            self._input_buttons(button_list, delay)
            self.currentKey = letter

        return complete_button_list

    def _input_buttons(self, button_list, delay):

        # iterate the button list and press the arrows
        for button in button_list:
            if button == 'left':
                self.roku.left()
                time.sleep(delay)
            if button == 'right':
                self.roku.right()
                time.sleep(delay)
            if button == 'up':
                self.roku.up()
                time.sleep(delay)
            if button == 'down':
                self.roku.down()
                time.sleep(delay)
            if button == 'select':
                self.roku.select()
                time.sleep(delay)

        # then select to choose the letter
        return

    def _get_button_list(self, currentKey, newKey):

        if currentKey == newKey: return [ 'select' ]

        button_list = []
        special_key = False


        if newKey in SPECIAL_CHARACTERS: special_key = True

        if newKey == ' ': newKey = 'V'
        if currentKey == ' ': currentKey = 'V'

        horizontal_direction, vertical_direction = self._get_key_directions(currentKey, newKey, special_key)

        self._get_concrete_path(horizontal_direction, vertical_direction, button_list)

        if special_key:
            button_list.extend(['down', 'select', 'up'] )
        else:
            button_list.append( 'select' )


        return button_list

    def _get_concrete_path(self, horizontal_direction, vertical_direction, button_list):
        if horizontal_direction > 0:
            for i in range(abs(horizontal_direction)):
                button_list.append('right')
        if horizontal_direction < 0:
            for i in range(abs(horizontal_direction)):
                button_list.append('left')
        if vertical_direction > 0:
            for i in range(abs(vertical_direction)):
                button_list.append('down')
        if vertical_direction < 0:
            for i in range(abs(vertical_direction)):
                button_list.append('up')

    def _get_key_directions(self, currentKey, newKey, special_key):
        if special_key:
            horizontal_direction = self._get_key_coords(newKey)[1] - self._get_key_coords(currentKey)[1]
            vertical_direction = self._get_key_coords(newKey)[0] - self._get_key_coords(currentKey)[0]
        else:
            horizontal_direction = self._get_key_coords(newKey)[1] - self._get_key_coords(currentKey)[1]
            vertical_direction = self._get_key_coords(newKey)[0] - self._get_key_coords(currentKey)[0]
        return horizontal_direction, vertical_direction

    def _get_key_coords(self, key):

        for row in self.YOUTUBEKEYBOARD:
            for row_key in row:
                if row_key == key:
                    column = row_key
                    return self.YOUTUBEKEYBOARD.index(row), row.index(column)



    def youtube_search_cursor(self, roku):
        pass
        # self.roku.left()
        # self.roku.up()
        # self.roku.right()
        # self.roku.right()