class A:

    def __init__(self, a_name, age):
        self.a_name = a_name
        self.age = age


class B:

    def __init__(self, b_name):

        self.b_name = b_name

class C(A, B):

    def __init__(self, a_name, age, b_name, c_name):
        self.c_name = c_name

        A.__init__(self, a_name, age)
        B.__init__(self, b_name)


obj = C('Rahul', 28, 'Singh', 'Yadav')
print(obj.a_name, obj.b_name, obj.c_name)