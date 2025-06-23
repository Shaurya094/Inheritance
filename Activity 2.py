class person:
               def __init__(self, name, id):
                               self.name = name
                               self.id = id
               def display(self):
                               print(self.name)
                               print(self.id)

class employee(person):
                def __init__ (self, name, id, salary, post):
                               self.salary = salary
                               self.post = post
                               person.__init__(self, name, id)

a = employee("Shaurya", 742572, 23452, "Intern")
a.display()