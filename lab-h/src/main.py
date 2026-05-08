import logging
import warnings

logging.captureWarnings(True)
logger = logging.getLogger(__name__)


class MyError(Exception):
    """An example custom exception"""

    pass


class MyWarning(UserWarning):
    """An example custom warning"""

    pass


def main():
    print("Hello from lab-h!")
    x = 99
    if x > 100:
        raise ValueError(f"x was {x}. It should be 100 or less.")

    warnings.warn("This is a custom warning from lab-h.", MyWarning)


if __name__ == "__main__":
    # Set up logging
    log_filename = "log.txt"
    logging.basicConfig(filename=log_filename, level=logging.WARNING)

    # Run main function
    main()
