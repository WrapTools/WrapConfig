# secrets.py

import logging
import configparser
from pathlib import Path

logger = logging.getLogger(__name__)


class SecretsManager:
    """
    A class for reading and writing key/value secrets from a .env file.
    This class does not use any third-party libraries and preserves only
    the key=value lines (commented and blank lines are discarded).

    Example usage:
    --------------
    secrets = SecretsManager(".env")
    secrets.set_secret("API_KEY", "12345")
    my_api_key = secrets.get_secret("API_KEY")
    """
    def __init__(self, env_file):
        self.env_file = Path(env_file)
        if not self.env_file.exists():
            self.env_file.touch()  # Create file if it doesn't exist
        self.secrets = {}
        self.load_secrets()

    def load_secrets(self):
        """Reads the .env file and loads all key=value pairs into a dictionary."""
        self.secrets.clear()
        with open(self.env_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                # Skip empty lines or comments
                if not line or line.startswith('#'):
                    continue
                # Key-Value pairs are assumed to be 'key=value'
                if '=' in line:
                    key, value = line.split('=', 1)
                    self.secrets[key.strip()] = value.strip()

    def get_secret(self, key):
        """Returns the value of the specified key, or None if it doesn't exist."""
        return self.secrets.get(key)

    def set_secret(self, key, value):
        """
        Sets or updates a secret, then immediately saves changes to disk.
        """
        self.secrets[key] = value
        self.save_secrets()

    def delete_secret(self, key):
        """
        Deletes a secret from the .env file (if it exists),
        then saves changes to disk.
        """
        if key in self.secrets:
            del self.secrets[key]
            self.save_secrets()

    def get_all_secrets(self):
        """
        Returns a copy of all secrets as a dictionary.
        """
        return dict(self.secrets)

    def save_secrets(self):
        """
        Writes the current dictionary of secrets to the .env file.
        (Comments and blank lines are not preserved.)
        """
        with open(self.env_file, 'w', encoding='utf-8') as f:
            for key, value in self.secrets.items():
                f.write(f"{key}={value}\n")
