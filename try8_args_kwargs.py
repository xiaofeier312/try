from functools import wraps


def log_deco(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('~~~start wrapper')
        func(*args, **kwargs)
        print('func was called, args is: ')
        print(args)
        print(kwargs)
        print('wrapper end.')

    return wrapper


@log_deco
def get_var(number, name='ab', **kwargs):
    pass


if __name__ == '__main__':
    get_var(1, 2, sa='ab', c='cd')
