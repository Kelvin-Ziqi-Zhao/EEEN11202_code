class Over100(Exception):
    """An example custom exception"""

    pass


def print_x(x):
    """Print x, but only if it is less than 100"""
    if x > 100:
        raise Over100(f"x was {x}. It should be 100 or less.")
    print(f"x is {x}")


def main():
    print("Hello from lab-h!")

    try:
        x = "hello"

        print_x(x)
    except Over100 as e:
        print(f"Caught an exception: {e}")
    except TypeError as e:
        print("I was expecting x to be a number!")
    else:
        print("No exceptions were raised.")
    finally:
        print(f"Done")


if __name__ == "__main__":
    main()
