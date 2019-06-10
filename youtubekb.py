import time
from flask_wtf import FlaskForm
from wtforms import StringField

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
            button_list.append('select')
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
                time.sleep(.2)
            if button == 'select':
                self.roku.select()
                time.sleep(.2)

        # then select to choose the letter
        return

    def _get_button_list(self, currentKey, newKey):

        directions = []
        horizontal_direction = self._get_key_coords(newKey)[1] - self._get_key_coords(currentKey)[1]
        vertical_direction = self._get_key_coords(newKey)[0] - self._get_key_coords(currentKey)[0]

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