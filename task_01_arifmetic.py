"""Написать программу вычисления арифметического выражения заданного строкой. Используются операции +,-,/,
*. приоритет операций стандартный. Функцию eval не использовать! Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
Дополнительно: Добавить возможность использования скобок, меняющих приоритет операций. Пример: 1+2*3 => 7; (1+2)*3 =>
9; """


def arith_expression(exp):
    def mult(exp):
        facts = exp.split('*')
        result = 1
        for i in facts:
            if '.' in i:
                result *= float(i)
            else:
                result *= int(i)
        return result

    def mult_or_div(exp):
        dividers = exp.split('/')
        result = mult(dividers[0])
        for i in dividers[1:]:
            result /= mult(i)
        return result

    "Проверка на скобки. Используем рекурсию для решения"
    while '(' in exp:
        "Ищем начало и конец выражения в скобках"
        index1 = exp.index('(')
        index2 = index1 + 1
        count = 1
        while count > 0:
            if exp[index2] == '(':
                count += 1
            if exp[index2] == ')':
                count -= 1
            index2 += 1
        "Выписываем полученное выражение в отдельную переменную"
        sub_exp = exp[index1 + 1:index2 - 1]
        in_brackets = arith_expression(sub_exp)
        exp = exp[:index1] + str(in_brackets) + exp[index2:]

    "Для удобства приводим все в виде слагаемых. Там где стоит - добавляем спереди +"
    exp = exp.replace('-', '+-').replace(' ', '')
    terms = exp.split('+')
    summ = 0
    for i in terms:
        summ += mult_or_div(i)
    return summ


# s = input('Введите арифметическое выражение: ')
# s = '2 + 3*(1/2 + 4/(5-3)) + 2*((1+2)*3 + 1)'
s = '2+(1+2)*3 + 3*(1/2 + 4/(5-3))'
# print(eval(s))
solution = arith_expression(s)
print(solution)
# print(solution == eval(s))
