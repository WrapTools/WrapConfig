import logging

# Logger Configuration
logger = logging.getLogger(__name__)

import sys
from pathlib import Path
from types import SimpleNamespace

class RuntimeConfig:
    """
    Singleton class to manage runtime settings.

    This class ensures that there is only one instance of runtime settings
    throughout the application.

    Attributes:
        program_dir (Path): The directory where the program is located.
        home_dir (Path): The home directory of the current user.
        ini_file_name (str or Path): The name or path of the INI file containing configuration settings.
        runtime_variables (SimpleNamespace): A namespace for runtime settings.

    Methods:
        get_program_dir(): Determines the program directory, handling both frozen and non-frozen states.

    Example:
        settings = RuntimeSettings()

    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        Ensures that only one instance of the class is created.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, ini_file_name=None):
        """
        Initializes the runtime settings.

        Args:
            ini_file_name (str or Path, optional): The name or path of the INI file. Defaults to 'settings.ini'
                in the program directory.
        """
        if self._initialized:
            return
        self._initialized = True

        self.program_dir = self.get_program_dir()
        self.home_dir = Path.home()
        self.ini_file_name = ini_file_name or self.program_dir / 'CRSettings.ini'
        self.runtime_variables = SimpleNamespace()

    @staticmethod
    def get_program_dir():
        """
        Determines the program directory.

        Returns:
            Path: The directory where the program is located.
        """
        if getattr(sys, 'frozen', False):
            # The application is frozen (bundled into an executable)
            return Path(sys.executable).parent
        else:
            # The application is not frozen (running from Python source)
            return Path(sys.argv[0]).parent

    def add_runtime_variable(self, name, value):
        """
        Adds a runtime setting to the runtime namespace.

        Args:
            name (str): The name of the setting.
            value: The value of the setting.
        """
        setattr(self.runtime_variables, name, value)

    def get_runtime_variable(self, name):
        """
        Retrieves a runtime setting from the runtime namespace.

        Args:
            name (str): The name of the setting.

        Returns:
            The value of the setting.
        """
        return getattr(self.runtime_variables, name, None)

    def delete_runtime_variable(self, name):
        """
        Deletes a runtime variable from the runtime namespace.

        Args:
            name (str): The name of the variable.
        """
        if hasattr(self.runtime_variables, name):
            delattr(self.runtime_variables, name)
