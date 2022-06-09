"""Entry point

Run `python main.py`

"""
import logging
import logging.config
import os


def main():
    """main function"""

    logging.config.fileConfig(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "logging.conf")
    )

    import example.module1  # import after applying log configuration

    logger = logging.getLogger(__name__)
    logger.info("main start")
    logger.debug("This is a debug message.")
    logger.info("This is an info message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    logger.critical("This is a critical message.")

    _sum1 = example.module1.mean([1, 2, 3])
    logger.info("Sum 1 to 3: %d", _sum1)

    try:
        1 / 0
    except ZeroDivisionError as err:
        logger.warning("exception", exc_info=err)
        # import sys
        # logger.debug("exception: {}".format(sys.exc_info()))

    logger.info("main end")


if __name__ == "__main__":
    main()
