import unittest
from youtubekb import YouTubeKeyboardController
from roku import Roku

class Test_youtubekb(unittest.TestCase):

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