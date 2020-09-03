import unittest

from linear import Linear


class TestLinearMethod(unittest.TestCase):

    def test_check_zero(self):
        point_1 = (0., 0.)
        point_2 = (0., 0.)
        linear = Linear(point_1, point_2)
        self.assertTrue(linear.compute_dist() == 0.)

    def test_check_pythagorean_theorem(self):
        point_1 = (12., -8.)
        point_2 = (0., 0.)
        linear = Linear(point_1, point_2)
        self.assertTrue(linear.compute_dist() == (12.**2 + 8.**2)**(0.5))

    def test_check_datatype(self):
        point_1 = [12., -8.]
        point_2 = {0., 0.}
        linear = Linear(point_1, point_2)
        self.assertTrue(linear.compute_dist() == 'Wrong datatype')

    def test_check_dimension(self):
        point_1 = (12., -8., 7.)
        point_2 = 4.
        linear = Linear(point_1, point_2)
        self.assertTrue(linear.compute_dist() == 'Wrong dimension')


if __name__ == '__main__':
    unittest.main()
