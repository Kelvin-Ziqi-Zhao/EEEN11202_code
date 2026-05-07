class ExampleClass:
    """
    Docstring for ExampleClass
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def multiply(self, factor):
        return self.value * factor


def main():
    # Create instances of ExampleClass
    a = ExampleClass(2)
    b = ExampleClass(3)
    c = ExampleClass(4)

    # Print values
    print(a.value)
    print(b.value)
    print(c.value)

    print(a.multiply(1))
    print(b.multiply(2))
    print(c.multiply(3))
    print(a)


if __name__ == "__main__":
    main()
