import logging
import sys

def setup_logger(name: str) -> logging.Logger:
    """Sets up a standardized logger for the application."""
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.INFO)
        # Format requested by assignment: "INFO Tool called: get_order ORD-1001"
        formatter = logging.Formatter('INFO %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger
