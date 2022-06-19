"""Написать программу вычисления арифметического выражения заданного строкой. Используются операции +,-,/,
*. приоритет операций стандартный. Функцию eval не использовать! Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
Дополнительно: Добавить возможность использования скобок, меняющих приоритет операций. Пример: 1+2*3 => 7; (1+2)*3 =>
9; """


def arith_expression(exp):
    def mult(exp):
        facts = exp.split('*')
        result = 1
        for i in facts:
            result *= int(i)
        return result

    def mult_or_div(exp):
        dividers = exp.split('/')
        result = mult(dividers[0])
        for i in dividers[1:]:
            result /= mult(i)
        return result

    exp = exp.replace('-', '+-').replace(' ', '')
    terms = exp.split('+')
    summ = 0
    for i in terms:
        summ += mult_or_div(i)
    return summ


# s = input('Введите арифметическое выражение: ')
s = '2+3-5*2 - 10/2/5'
solution = arith_expression(s)
print(solution)
print(solution == eval(s))