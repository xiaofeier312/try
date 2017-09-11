class OldClass:
    pass


class NewClass(object):
    pass


print('old class is: {}'.format(type(OldClass)))
print('new class is: {}'.format(type(NewClass)))
