class Store :
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def total_order(self):
        return (self.i + self.j)

    # class method
    @classmethod
    def clsorder(cls, double):
        return cls(double, double)

order1 = Store(3,2)
print(order1.total_order())

order2 = Store.clsorder(3)
print(order2.total_order())