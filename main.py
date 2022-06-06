import application.salary as sal
import application.db.people as peop
from datetime import date

if __name__ == '__main__':
    print(date.today())
    sal.calculate_salary()
    peop.get_employees()
