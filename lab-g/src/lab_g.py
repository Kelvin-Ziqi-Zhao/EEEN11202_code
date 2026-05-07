import math

# comment


class RcFilter:
    def __init__(self, r, c):
        self.r = r
        self.c = c

    def __str__(self):
        return str(f"r={self.r}, c={self.c}")

    def get_email_address(self):
        return "RcFilter object by student ziqi.zhao-5@student.manchester.ac.uk"

    def set_resistance(self, r):
        self.r = r

    def set_capacitance(self, c):
        self.c = c

    def get_cutoff(self):
        return 1 / (2 * math.pi * self.r * self.c)


if __name__ == "__main__":
    a = RcFilter(1, 2)
    print(a)
    a.set_resistance(2)
    a.set_capacitance(3)
    print(a)
    print(a.get_email_address())
    print(a.get_cutoff())
