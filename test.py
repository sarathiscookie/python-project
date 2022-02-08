class Salary:
    min_salary_per_day = 15

    def __init__(self, name: str, age: int, working_days: int, salary_per_day: float):
        assert 10 < working_days, f"You have to arrange a meeting with your manager. Your attendance is very low {working_days}."

        self.name = name
        self.age = age
        self.working_days = working_days
        self.salary_per_day = salary_per_day

    def calculate_total_salary(self):
        return self.working_days * self.salary_per_day

    def calculate_minimum_salary(self):
        return self.min_salary_per_day * self.working_days

salary = Salary("Peter", 35, 11, 25)
print(Salary.__dict__)
print(salary.__dict__)







