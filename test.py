import fire


def function1(arg1, arg2):
    # Code for function 1
    print(1)
    pass


def function2(arg1, arg2):
    # Code for function 2
    print(2)
    pass


if __name__ == '__main__':
    fire.Fire({
        'function1': function1,
        'function2': function2
    })
