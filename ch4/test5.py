alist = [0]*6

def returnNone(anyList):
    """
    :param anyList: any list object of which length is greater than zero
    :return: None
    This function is used to show how arguments are changed in place in the function.

    The object reference is passed to the function parameters.
    They can't be changed within the function, because they can't be changed at all, i.e. they are immutable.
    It's different, if we pass mutable arguments. They are also passed by object reference,
    but they can be changed in place in the function.
    """
    anyList[0] = 1

    return

returnNone(alist)
print(alist)