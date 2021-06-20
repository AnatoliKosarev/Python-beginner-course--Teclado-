class Employee:
    def __init__(self, name: str, lastname: str, yearly_salary: float):
        self.name = name
        self.lastname = lastname
        self.yearly_salary = yearly_salary

    def give_raise(self, raise_amount=5000.00) -> None:
        self.yearly_salary += raise_amount
