
class A:

    def __init__(self, a_name, age):
        self.a_name = a_name
        self.age = age
    
class B(A):

    def __init__(self,a_name, age ,b_name):
        self.b_name = b_name
        super().__init__(a_name, age)


obj = B('Rahul', 28, 'yadav')

print(obj.a_name, obj.b_name)




