import unittest
from task_1.main import Circle, Triangle


class TestShapes(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(3)
        self.assertAlmostEqual(circle.get_area(), 28.274333882308138)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.get_area(), 6.0)

    def test_triangle_right_angle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_angle())


if __name__ == "__main__":
    unittest.main()
