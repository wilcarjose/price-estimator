# config/logging.py

import logging
import sys
import os

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

def get_logger(name: str) -> logging.Logger:
    """
    Configures and returns a logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.propagate = False  # Prevents log duplication

    # Prevents adding multiple handlers if the logger is already configured.
    if not logger.handlers:
        # Console Handler
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(logging.Formatter(LOG_FORMAT))
        logger.addHandler(stream_handler)

        # File Handler
        file_handler = logging.FileHandler(os.path.join(LOG_DIR, "app.log"))
        file_handler.setFormatter(logging.Formatter(LOG_FORMAT))
        logger.addHandler(file_handler)

    return logger
