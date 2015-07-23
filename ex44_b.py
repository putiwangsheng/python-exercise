class Other(object):

    def override(self):
        print("other override()")

    def implicit(self):
        print("other implicit()")

    def altered(self):
        print("other altered()")

class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("Child override()")

    def altered(self):
        print("Child, before other altered()")
        self.other.altered()
        print("Child, after other altered()")

son = Child()

son.implicit()
son.override()
son.altered()
