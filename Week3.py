def my_function (*params):
    S = 0
    for element in params:
        if isinstance(element, int) or isinstance(element, float):
           S += element
    return S


print("Function return value: ", my_function(1, 5, -3, 'abc', [12, 56, 'CAD']))


def zero_to_n (n: int):
    if n == 0:
        return 0
    else:
        return n+zero_to_n(n-1)

print("Function sum result: ",zero_to_n(8))


def evens_zero_to_n(n: int):
    if n == 0:
        return 0
    elif  n % 2 ==0:
        return n+evens_zero_to_n(n-2)
    else:
        return evens_zero_to_n(n-1)

print("Function evens sum result: ",evens_zero_to_n(8))


def odds_zero_to_n(n: int):
    if n==0:
        return 0
    elif n == 1:
        return 1
    elif n % 2 !=0:
        return n + odds_zero_to_n(n-2)
    else:
        return odds_zero_to_n(n-1)

print("Function odds sum result: ",odds_zero_to_n(8))


def input_checker():
    my_input =input("Please input something: ")
    flag = None
    try:
        int(my_input)
        flag =True
    except ValueError:
        flag = False

    if flag:
        return int(my_input)
    else:
        return 0


print(input_checker())