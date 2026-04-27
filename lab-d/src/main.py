def main():
    print("Hello from lab-d!")
    x = 9
    y = 5
    if x > y:
        print(f"x is greater than {y}")
    elif x == y:
        print(f"x is {y}")
    elif x < y:
        print(f"x is less than {y}")
    else:
        raise ValueError("Unexpected comparison result")


if __name__ == "__main__":
    a = 56  # used in the next part of the lab
    x = 3.54  # used in the next part of the lab
    main()
