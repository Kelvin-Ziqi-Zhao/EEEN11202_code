import pathlib
from os.path import join as pjoin


class NotMyEmail(Exception):
    pass


def read_email_file():
    # Get the path to the .txt file
    # This uses pathlib to automatically get the folder where this script is located and navigates from there
    script_folder = pathlib.Path(__file__).parent.resolve()
    data_dir = pjoin(script_folder, "../", "data")
    fname = pjoin(data_dir, "email.txt")
    fname_backup = pjoin(data_dir, "backup.txt")

    # Load data
    try:
        with open(fname) as f:
            lines = f.readlines()[0]
    except FileNotFoundError:
        with open(fname_backup) as f:
            lines = f.readlines()[0]

    return lines
    # Add code here


if __name__ == "__main__":
    # Add code here
    email = read_email_file()
    if email == "ziqi.zhao-5@student.manchester.ac.uk":
        print("True")
    else:
        raise NotMyEmail("Incorrect email address.")

# comment
