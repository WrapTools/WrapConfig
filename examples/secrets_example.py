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


from WrapConfig import SecretsManager

def main():
    # Instantiate the manager with the name of your .env file
    secrets = SecretsManager(".env")

    # 1. Set some secrets
    secrets.set_secret("API_KEY", "12345")
    secrets.set_secret("DB_PASSWORD", "MySecurePassword")

    # 2. Retrieve a secret
    api_key = secrets.get_secret("API_KEY")
    print("API_KEY:", api_key)

    # 3. Get all secrets
    all_secrets = secrets.get_all_secrets()
    print("All secrets:", all_secrets)

    # 4. Delete a secret
    secrets.delete_secret("DB_PASSWORD")

    # 5. Check that it's really gone
    print("DB_PASSWORD after deletion:", secrets.get_secret("DB_PASSWORD"))

    # 6. Retrieve remaining secret
    api_key = secrets.get_secret("API_KEY")
    print("API_KEY:", api_key)

if __name__ == "__main__":
    main()