class OuterClass:

    def __init__(self, name):
        self.name = name
        self.lg = self.InnerClass()

    class InnerClass:
        def __init__(self):
            self.inner_name = 'Inner class'

        def display(self):
            return self.inner_name
        

OU = OuterClass('Rahul')

g = OU.lg

print(g.display())