def sum(a, b):
    return a + b


def razn(a, b):
    return a - b


def umn(a, b):
    return a * b


def delen(a, b):
    return a / b


formula = '23+32*2/4'
array = []
for i in range(0, len(formula)):
    if formula[i] == '+' or formula[i] == '-' or formula[i] == '*' or formula[i] == '/':
        array.append(formula[i])
formula = formula.replace('+', ' ')
formula = formula.replace('-', ' ')
formula = formula.replace('*', ' ')
formula = formula.replace('/', ' ')
formula = formula.split(' ')
res = formula[0]
print(array)
for i in range(0, len(array)):
    if array[i] == '+':
        res = sum(int(res), int(formula[i + 1]))
    if array[i] == '-':
        res = razn(int(res), int(formula[i + 1]))
    if array[i] == '*':
        res = umn(int(res), int(formula[i + 1]))
    if array[i] == '/':
        res = delen(int(res), int(formula[i + 1]))


print(res)