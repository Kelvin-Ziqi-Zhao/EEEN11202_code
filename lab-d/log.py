import logging

logger = logging.getLogger(__name__)


def countdown(x):
    countdown = range(x, -1, -1)
    for i in countdown:
        print(f"{i}")
        logger.warning(f"{i}")
    print("Blast off")


def check_x():
    logger.info("Hello from lab-d!")
    x = 9
    y = 5
    if x > y:
        logger.info(f"x is greater than {y}")
    elif x == y:
        logger.info(f"x is {y}")
    elif x < y:
        logger.info(f"x is less than {y}")
    else:
        raise ValueError("Unexpected comparison result")

    countdown(x)


def main():
    # Set up logging
    log_filename = "log.txt"
    logging.basicConfig(filename=log_filename, level=logging.WARNING)
    logger.info("Started")

    # Run wanted functions
    a = 56  # used in the next part of the lab
    x = 3.54  # used in the next part of the lab
    check_x()

    # Tidy up logging
    logger.info("Finished")


if __name__ == "__main__":
    main()
