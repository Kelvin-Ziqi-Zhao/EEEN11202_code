"""
Template code for Lab C
"""


 def main():
    min = None
    # Solution code - Enter your code here
    filename = "numbers.csv"
    with open(filename, "r") as f:
        for line in f:
            # print(min)
            num = float(line.strip())

            if num >= 10:
                if min == None or num <= min:
                    min = num

    # print(min)

    output_filename = "output.txt"
    with open(output_filename, "w") as f:
        if min == None:
            f.write("Error")
        else:
            f.write(str(min))
        f.write("\n")
        f.write("Hello. My email address is:\n")
        f.write("ziqi.zhao-5@student.manchester.ac.uk")

    return


if __name__ == "__main__":
    # Solution code - Enter your code here
    main()
