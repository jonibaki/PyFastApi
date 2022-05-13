from Calculator import Calculator

if __name__ == '__main__':
    calculator = Calculator()
    first_num = int(input("Enter the first number: "))
    second_num = int(input("Enter the second number: ",))
    op = input("Type operation symbol(+, -, *, /) : ")
    if op == '+':
        add = calculator.add_two_numbers(first_num, second_num)
        print(f'{first_num} {op} {second_num} = {add}')

    elif op == '-':
        subtract = calculator.subtract_two_numbers(first_num, second_num)
        print(f'{first_num} {op} {second_num} = {subtract}')

    elif op == '*':
        multiply = calculator.multiply_two_numbers(first_num, second_num)
        print(f'{first_num} {op} {second_num} = {multiply}')

    elif op == '/':
        divide = calculator.divide_two_numbers(first_num, second_num)
        print(f'{first_num} {op} {second_num} = {divide}')

    elif op == '':
        print('null is not a valid operator sign!')
    else:
        print(f'{op} is not a valid operator sign!')


