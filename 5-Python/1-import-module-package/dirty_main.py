from datetime import *
from application import salary
from application.db import people

if __name__ == '__main__':
    print(datetime.datetime.now())
    salary.salary()
    people.get_employees()


