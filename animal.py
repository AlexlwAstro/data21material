class Animal:
    def __init__(self):
        self.spine = True
        self.alive = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        print('one breath in, one breath out')

    def eat(self):
        print('nom nom nom')

    def moving(self):
        print('Forwards, backwards, sideways')


if __name__ == 'animal':
    cat = Animal()
    cat.breathe()
    print(__name__)
