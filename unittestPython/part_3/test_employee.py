import unittest

from HelloWorld.unittestPython.part_3.employee import Employee


class EmployeeTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.employee = Employee("John", "Smith", 15000.00)

    def test_give_default_raise(self) -> None:
        self.employee.give_raise()
        self.assertEqual(self.employee.yearly_salary, 20000.00)

    def test_give_custom_raise(self) -> None:
        self.employee.give_raise(2000.51)
        self.assertEqual(self.employee.yearly_salary, 17000.51)
