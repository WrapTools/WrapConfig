# runtime_example.py

# Configure Logging
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format = '%(name)s - %(levelname)s - %(message)s (line: %(lineno)d)',
    handlers=[
        logging.StreamHandler(),  # Log to console
        # logging.FileHandler('app.log')  # Log to file
    ]
)
logger = logging.getLogger(__name__)


from WrapConfig import RuntimeConfig


def main():
    # Initialize the RuntimeConfig instance
    config = RuntimeConfig()

    # Log the program and home directories
    logger.info(f"Program Directory: {config.program_dir}")
    logger.info(f"Home Directory: {config.home_dir}")

    # Add runtime variables
    config.add_runtime_variable('api_key', '12345-abcde')
    config.add_runtime_variable('use_ssl', True)

    # Retrieve and log runtime variables
    logger.info(f"API Key: {config.get_runtime_variable('api_key')}")
    logger.info(f"Use SSL: {config.get_runtime_variable('use_ssl')}")

    # Delete a runtime variable
    config.delete_runtime_variable('api_key')

    # Try to retrieve the deleted variable
    logger.info(f"API Key (after deletion): {config.get_runtime_variable('api_key')}")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()