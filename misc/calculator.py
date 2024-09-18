def calculator( a, operation, b ):
    '''
    Calculator fuction takes in numbers a and b, and an operation called operation.
    Returns the needed calculation.
    '''
    a = float( a )
    b = float( b )

    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a*b
    elif operation == '/':
        if b == 0:
            return 'Can not devide by 0.'
        return a / b
    else:
        return 'Operation not supported.'

need_to_compute = '1+1'
output = calculator( need_to_compute[0], need_to_compute[1], need_to_compute[2] )
print(output)


def sqaured( n ):
    output = n * n
    return output

def hello( name, age ):
    print(f'Hello, {name}. You are {age} of age.')
    return 1

# print( sqaured( 4 ) )


# hello( 'Zack', '23')
# returned = hello()
# print(returned)