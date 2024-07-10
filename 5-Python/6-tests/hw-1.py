def square_calculation(a):
    perimeter = 4*a  # Расчёт периметра
    area = a*a # Расчёт площади
    return perimeter, area

def rectangle_calculation(a,b):
    perimeter = a*2+2*b # Расчёт периметра
    area = a*b # Расчёт площади
    return perimeter, area

def phinance(salary, percent_mortgage, percent_life):
    # Напишите свой код здесь
    mortgage = 12* salary * percent_mortgage * .01
    result = 12 * (salary - percent_mortgage * 0.01 * salary 
                   - percent_life * 0.01* salary)
    return mortgage, result

print(square_calculation(1))

def test():
    assert square_calculation(1) == (4, 1)

