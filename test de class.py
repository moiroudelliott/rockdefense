class fruit():
    def __init__(self):
        self.elt = "yop"

    def strB(self):
        print("top")

class pomme(fruit):
    def __init__(self, nom):
        fruit.__init__(self)
        self.nom = nom

    def str(self):
        print(self.nom)

def test():
    print("Hello world")

dispatcher={'test':test}
w='test'
try:
    function=dispatcher[w]
except KeyError:
    raise ValueError('invalid input')