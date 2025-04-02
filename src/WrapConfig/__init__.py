import logging

# Create a logger for your library
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

# __all__ = ['Class']

def test_function():
    logger.debug("This is a debug message from WrapConfig.")

from .ini_config import INIHandler
from .runtime_config import RuntimeConfig
from .secrets_config import SecretsManager
