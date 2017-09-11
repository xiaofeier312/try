class Person:
    def __init__(self):
        self.__name__ = 'docker'
        self._say = 'co'



p=Person()

print (p.__name__)
print (p._say)

print(('{1} at {0} is {1}').format('k','kk'))
print (p.__dict__)