class A:
    def method(self):
        print(self)

    @classmethod
    def class_method(cls):
        print(cls)

    @staticmethod
    def static_method():
        print('static_method')

a = A()
a.method()        # <__main__.A object at 0x7f7f62d47a20>
A.class_method()  # <class '__main__.A'>
A.static_method() #
