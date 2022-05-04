import unittest



class MyTestCase(unittest.TestCase):
    def test_clicked(self):
        with self.assertRaises(TypeError):
            clicked(10)
        with self.assertRaises(TypeError):
            clicked(10.0)


if __name__ == '__main__':
    unittest.main()
