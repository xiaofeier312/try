class A():
    def method(self):
        print('i mm method')
    @staticmethod
    def static_m():
        print ('i am static me')
    @classmethod
    def class_m(cls):
        print ('i am class method')


if __name__ == "__main__":
    a = A()
    a.method()
    a.class_m()
    a.static_m()
    print('\n')
    A.static_m()
    A.class_m()
    A.method(a)
    print("type(A): {}".format(type(A)))
    print(dir(A))