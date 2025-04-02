# ini_config.py

import logging

# Logger Configuration
logger = logging.getLogger(__name__)

import configparser
from pathlib import Path


class INIHandler:
    def __init__(self, file_path):
        self.file_path = Path(file_path)
        self.config = configparser.ConfigParser()
        if not self.file_path.exists():
            self.file_path.touch()
        self.config.read(self.file_path)

    def reload(self):
        self.config.read(self.file_path)

    def create_or_update_option(self, section_name, option_name, value):
        if not self.config.has_section(section_name):
            self.config.add_section(section_name)
        self.config.set(section_name, option_name, value)

    def read_sections(self):
        return self.config.sections()

    def read_options(self, section_name):
        if self.config.has_section(section_name):
            return self.config.options(section_name)
        else:
            return []

    def read_value(self, section_name, option_name, refresh=False):
        if refresh:
            self.config.read(self.file_path) # if values can change and ini file may be cached, refresh file
        try:
            return self.config.get(section_name, option_name)
        except (configparser.NoSectionError, configparser.NoOptionError):
            return None

    def check_section_exists(self, section_name):
        return self.config.has_section(section_name)

    def check_option_exists(self, section_name, option_name):
        return self.config.has_option(section_name, option_name)

    def get_all_options_with_values(self, section_name):
        if self.config.has_section(section_name):
            return dict(self.config.items(section_name))
        else:
            return {}

    def delete_option(self, section_name, option_name):
        try:
            self.config.remove_option(section_name, option_name)
        except configparser.NoSectionError:
            print(f"Section '{section_name}' does not exist.")
        except configparser.NoOptionError:
            print(f"Option '{option_name}' does not exist in section '{section_name}'.")

    def delete_section(self, section_name):
        try:
            self.config.remove_section(section_name)
        except configparser.NoSectionError:
            print(f"Section '{section_name}' does not exist.")

    def rename_section(self, old_section_name, new_section_name):
        if old_section_name in self.config.sections():
            if new_section_name in self.config.sections():
                print(f"Section '{new_section_name}' already exists.")
                return
            options = self.config.items(old_section_name)
            self.config.add_section(new_section_name)
            for option, value in options:
                self.config.set(new_section_name, option, value)
            self.config.remove_section(old_section_name)
        else:
            print(f"Section '{old_section_name}' does not exist.")

    def clear_section(self, section_name):
        try:
            for option in self.read_options(section_name):
                self.delete_option(section_name, option)
        except configparser.NoSectionError:
            print(f"Section '{section_name}' does not exist.")

    def save_changes(self):
        with open(self.file_path, 'w', encoding='utf-8') as config_file:
            self.config.write(config_file)   # type: ignore


class RecentFilesManager:
    def __init__(self, config_path, num_of_files=5, ini_section=None):
        self.config_path = Path(config_path)
        self.num_of_files = num_of_files
        self.ini_section = ini_section if ini_section else 'RecentFiles'
        self.config = configparser.ConfigParser()
        self.recent_files = self.load_recent_files()

    def load_recent_files(self):
        self.config.read(self.config_path)
        if self.ini_section in self.config:
            return [self.config[self.ini_section][f"file{i}"] for i in range(1, self.num_of_files + 1) if
                    f"file{i}" in self.config[self.ini_section]]
        else:
            return []

    def add_file(self, file_path):
        if file_path in self.recent_files:
            self.recent_files.remove(file_path)
        self.recent_files.insert(0, file_path)
        self.recent_files = self.recent_files[:self.num_of_files]
        self._save_to_file()

    def get_recent_files(self):
        return self.recent_files

    def _save_to_file(self):
        if self.ini_section not in self.config:
            self.config.add_section(self.ini_section)
        for index, file in enumerate(self.recent_files):
            self.config.set(self.ini_section, f"file{index + 1}", file)
        with open(self.config_path, 'w') as configfile:
            self.config.write(configfile)   # type: ignore
