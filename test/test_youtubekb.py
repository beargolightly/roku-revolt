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
        self.yt = YouTubeKeyboardController(self.roku)

    def test_type_phrase__mockingtest(self):
        self.roku.up()
        self.roku.left()
        self.roku.left()
        self.roku.left()
        #self.yt.type_phrase('stuff', 'A')
        self.assertEqual(self.roku.left.call_count, 3)

    def test_type_phrase__stuff(self):
        self.yt.type_phrase('STUFF', 'A')
        self.assertEqual(self.yt.currentKey, 'F')


class Test_get_key_coords(unittest.TestCase):

    def setUp(self):
        self.roku = Roku('127.0.0.1')
        self.yt = YouTubeKeyboardController(self.roku)

    def test_get_key_coords_A(self):
        result = self.yt._get_key_coords('A')
        self.assertEqual(result, (0,0))

    def test_get_key_coords_D(self):
        result = self.yt._get_key_coords('D')
        self.assertEqual(result, (0,3))

    def test_get_key_coords_Z(self):
        result = self.yt._get_key_coords('Z')
        self.assertEqual(result, (3,4))

    def test_get_key_coords_Q(self):
        result = self.yt._get_key_coords('Q')
        self.assertEqual(result, (2,2))

class Test_get_key_directions(unittest.TestCase):

    def setUp(self):
        self.roku = Roku('127.0.0.1')
        self.yt = YouTubeKeyboardController(self.roku)

    def test_A_to_B(self):
        result = self.yt._get_key_directions('A','B')
        self.assertEqual(result, ['right'])

    def test_A_to_X(self):
        result = self.yt._get_key_directions('A','X')
        self.assertEqual(result, ['right', 'right', 'down', 'down', 'down'])

    def test_A_to_A(self):
        result = self.yt._get_key_directions('A', 'A')
        self.assertEqual(result, [])

class Test_input_buttons(unittest.TestCase):

    def setUp(self):
        self.roku = Mock(Roku('127.0.0.1'))
        self.roku.left = Mock()
        self.roku.right = Mock()
        self.roku.up = Mock()
        self.roku.down = Mock()
        self.roku.select = Mock()
        self.yt = YouTubeKeyboardController(self.roku)

    def test_basic_button_function(self):
        button_list = ['right', 'left', 'up', 'down']
        self.yt._input_buttons(button_list)

        self.yt.roku.left.assert_called()
        self.yt.roku.right.assert_called()
        self.yt.roku.up.assert_called()
        self.yt.roku.down.assert_called()
        self.yt.roku.select.assert_called()

    def test_upup_downdown_leftright_leftright_select(self):
        button_list = ['up', 'up', 'down', 'down', 'left', 'right', 'left', 'right']
        self.yt._input_buttons(button_list)

        self.assertEqual(self.yt.roku.left.call_count, 2)
        self.assertEqual(self.yt.roku.up.call_count, 2)
        self.assertEqual(self.yt.roku.right.call_count, 2)
        self.assertEqual(self.yt.roku.down.call_count, 2)
        self.assertEqual(self.yt.roku.select.call_count, 1)