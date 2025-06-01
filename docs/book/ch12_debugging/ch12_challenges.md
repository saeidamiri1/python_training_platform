---
title: Challenges
---
# Challenge

### Challenge 1
Write a class that takes a salary as input, and raises an error if the salary is not within the range of 5000 to 15000.

<details><summary>Respond:</summary>
```{Python, echo = FALSE, message = FALSE}
class SalaryNotInRangeError(Exception):
    """Exception raised for errors in the input salary.
    Attributes:
        salary -- input salary which caused the error
        message -- explanation of the error
    """
    def __init__(self, salary, message="Salary is not in (5000, 15000) range"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return f'{self.salary} -> {self.message}'


salary = int(input("Enter salary amount: "))
if not 5000 < salary < 15000:
    raise SalaryNotInRangeError(salary)
```
</details>

