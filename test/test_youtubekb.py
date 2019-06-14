import unittest
from unittest.mock import Mock
from youtubekb import YouTubeKeyboardController
from roku import Roku

class Test_type_phrase(unittest.TestCase):
    def setUp(self):
        self.roku = Mock(Roku('127.0.0.1'))
        self.roku.left = Mock()
        self.roku.right = Mock()
        self.roku.up = Mock()
        self.roku.down = Mock()
        self.roku.select = Mock()
        self.yt = YouTubeKeyboardController(self.roku, 'A')


    def test_type_phrase__currentKey(self):
        self.yt.type_phrase('STUFF', 0)
        self.assertEqual(self.yt.currentKey, 'F')


    def test_type_phrase__complete_button_list(self):
        result = self.yt.type_phrase('STUFF', 0)
        self.assertEqual(result, ['right', 'right', 'right', 'right', 'down', 'down', \
                                   'select', 'right', 'select', 'right', 'select', 'left', \
                                   'up', 'up', 'select', 'select'])


    def test_type_phrase__typing_stuff(self):
        self.yt.type_phrase('STUFF', 0)

        self.assertEqual(1, self.yt.roku.left.call_count)
        self.assertEqual(2, self.yt.roku.up.call_count)
        self.assertEqual(6, self.yt.roku.right.call_count)
        self.assertEqual(2, self.yt.roku.down.call_count)
        self.assertEqual(5, self.yt.roku.select.call_count)

    def test_type_phrase__with_a_space(self):
        self.yt.type_phrase('O P', 0)

        self.assertEqual(self.yt.roku.left.call_count, 0)
        self.assertEqual(self.yt.roku.up.call_count, 2)
        self.assertEqual(self.yt.roku.right.call_count, 1)
        self.assertEqual(self.yt.roku.down.call_count, 4)
        self.assertEqual(self.yt.roku.select.call_count, 3)


class Test_get_key_coords(unittest.TestCase):

    def setUp(self):
        self.roku = Roku('127.0.0.1')
        self.yt = YouTubeKeyboardController(self.roku, 'A')

    def test_get_key_coords_A(self):
        result = self.yt._get_key_coords('A')
        self.assertEqual((0,0), result)


    def test_get_key_coords_D(self):
        result = self.yt._get_key_coords('D')
        self.assertEqual((0,3), result)

    def test_get_key_coords_Z(self):
        result = self.yt._get_key_coords('Z')
        self.assertEqual((3,4), result)

    def test_get_key_coords_Q(self):
        result = self.yt._get_key_coords('Q')
        self.assertEqual((2,2), result)

class Test_get_key_directions(unittest.TestCase):

    def setUp(self):
        self.roku = Roku('127.0.0.1')
        self.yt = YouTubeKeyboardController(self.roku, 'A')

    def test_A_to_B(self):
        result = self.yt._get_button_list('A', 'B')
        self.assertEqual(['right', 'select'], result)

    def test_A_to_X(self):
        result = self.yt._get_button_list('A', 'X')
        self.assertEqual(['right', 'right', 'down', 'down', 'down', 'select'], result)

    def test_A_to_A(self):
        result = self.yt._get_button_list('A', 'A')
        self.assertEqual(['select'], result)

    def test_O_to_space(self):
        result = self.yt._get_button_list('O', ' ')

        button_list = [ 'down', 'down', 'select', 'up' ]
        self.assertEqual(button_list, result)

    def test_a_whole_phrase(self):
        result = self.yt._get_button_list

class Test_input_buttons(unittest.TestCase):

    def setUp(self):
        self.roku = Mock(Roku('127.0.0.1'))
        self.roku.left = Mock()
        self.roku.right = Mock()
        self.roku.up = Mock()
        self.roku.down = Mock()
        self.roku.select = Mock()
        self.yt = YouTubeKeyboardController(self.roku, 'A')

    def test_basic_button_function(self):
        button_list = ['right', 'left', 'up', 'down']
        self.yt._input_buttons(button_list, 0)

        self.yt.roku.left.assert_called()
        self.yt.roku.right.assert_called()
        self.yt.roku.up.assert_called()
        self.yt.roku.down.assert_called()

    def test_upup_downdown_leftright_leftright_select(self):
        button_list = ['up', 'up', 'down', 'down', 'left', 'right', 'left', 'right']
        self.yt._input_buttons(button_list, 0)

        self.assertEqual(self.yt.roku.left.call_count, 2)
        self.assertEqual(self.yt.roku.up.call_count, 2)
        self.assertEqual(self.yt.roku.right.call_count, 2)
        self.assertEqual(self.yt.roku.down.call_count, 2)


