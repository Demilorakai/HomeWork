class Fraction:
    def __init__(self, numertor, denumerator):
          self.numetor = numertor
          self.denumerator = denumerator

    def __add__(self, other):
            self.numetor += other
            self.denumerator += other
            print(self.numetor)
            return Fraction(self.numetor, self.denumerator)

    def __sub__(self, other):
        self.numetor -= other
        self.denumerator -= other
        print(self.numetor)
        return Fraction(self.numetor, self.denumerator)

    def __mul__(self, other):
            self.numetor *= other
            self.denumerator *= other
            print(self.numetor)
            return Fraction(self.numetor, self.denumerator)

    def __floordiv__(self, other):
            self.numetor //= other
            self.denumerator //= other
            print(self.numetor)
            return Fraction(self.numetor, self.denumerator)

num = Fraction(20, 20)

num_add = num + 10 + 10
num_sub = num - 10 - 10
num_mul = num * 2 * 2
num_floordiv = num // 3 // 2
