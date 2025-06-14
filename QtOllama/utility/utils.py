# utils.py
import logging

logger = logging.getLogger(__name__)

def handle_exception(e):
    """
    Logs an exception with error level and includes the traceback information.

    Args:
        e (Exception): The exception instance to be logged.
    """
    logger.error(f"{e}", exc_info=True)