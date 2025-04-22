class parent:

    def __init__(self, parrent_name):
        self.parrent_name = parrent_name

    
class child1(parent):

    def __init__(self, parrent_name, child1_name):
        self.child1_name = child1_name
        super().__init__(parrent_name)


class child2(parent):
    
    def __init__(self, parrent_name, child2_name):
        self.child2_name = child2_name
        super().__init__(parrent_name)


child1_name = child1('Sajnath', 'Rahul')
child2_name = child2('Sajnath', 'Khushbu')

print(child1_name.parrent_name, child1_name.child1_name)
print(child2_name.parrent_name, child2_name.child2_name)