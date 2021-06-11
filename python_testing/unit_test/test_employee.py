import unittest
from unittest.mock import patch
from employee import Employee

'''
our tests do NOT run in the order they have been written so they should be isolated from each other.
'''

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("runs before anything")

    @classmethod
    def tearDownClass(cls):
        print("runs after everything")

    # runs before every single test
    def setUp(self):
        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)

    # runs after every single test
    def tearDown(self):
        pass

    def test_email(self):
        self.assertEqual(self.emp_1.email, 'Corey.Schafer@gmail.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@gmail.com')

        self.emp_2.first = 'Jane'
        self.assertEqual(self.emp_2.email, 'Jane.Smith@gmail.com')

    def test_apply_raise(self):
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertNotEqual(self.emp_2.pay, 65000)

    '''
    here we don't actually care about the data that the website returns
    we want to make sure the get method uses the given url correctly to download data
    '''
    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.ir/Schafer/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_1.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.ir/Schafer/June')
            self.assertEqual(schedule, 'Bad Response!')


if __name__ == '__main__':
    unittest.main()




