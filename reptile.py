from animal import Animal


class Reptile(Animal):
    def __init__(self):
        super().__init__()
        self.cold_blooded = True

    def moving(self):
        print('Moving like a snake')

    def use_venom(self):
        print('if venom, will use')

    def __repr__(self):
        return f'This is a reptile'

    def __str__(self):
        return f'str version of This is a reptile'


bob = Reptile()
cat = Animal()
bob.moving()
cat.moving()

print(bob)
"""if __name__ == '__main__':
    cat = Animal()
    cat.breathe()
    print(__name__)"""