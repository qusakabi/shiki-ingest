import logging

def setup_logging():
    """
    Configures logging for the application.

    Returns:
        logging.Logger: A logger object.
    """
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    return logging.getLogger(__name__)

logger = setup_logging()