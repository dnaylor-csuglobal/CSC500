
def some_precondition():
    return True


def some_other_precondition():
    return True


def do_work():
    pass


def some_function():
    if not some_precondition():
        return
    if not some_other_precondition():
        return
    do_work()


def some_other_function():
    if some_precondition():
        if some_other_precondition():
            do_work()







