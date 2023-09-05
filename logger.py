import logging
from datetime import datetime

from pythonjsonlogger import jsonlogger


def init_logger() -> None:
    # Get today's date in the required format
    today = datetime.now().strftime("%Y-%m-%d")

    # Define the log file path
    log_file_path = f"logs/{today}.log"

    # Create a custom logger
    logger = logging.getLogger()

    # Set level of logging for the logger
    logger.setLevel(logging.INFO)

    # Create handlers
    c_handler = logging.StreamHandler()
    f_handler = logging.FileHandler(log_file_path)

    # Set level of logging for each handler
    c_handler.setLevel(logging.INFO)
    f_handler.setLevel(logging.INFO)

    # Create formatters and add it to handlers
    json_formatter = jsonlogger.JsonFormatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    c_format = json_formatter
    f_format = json_formatter

    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)

    # Add handlers to the logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)
