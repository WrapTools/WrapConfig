# ini_example.py

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

from WrapConfig.ini_config import INIHandler, RecentFilesManager

def main():
    # Assume we have a config file named 'example.ini' with the following content:
    """
    [Settings]
    username = admin
    password = pass123

    [Database]
    host = localhost
    port = 3306
    """
    # Instantiate the INIHandler with the file path
    config_handler = INIHandler('example.ini')

    # Create or update options for Settings
    config_handler.create_or_update_option('Settings', 'username', 'admin')
    config_handler.create_or_update_option('Settings', 'password', 'pass123')
    config_handler.create_or_update_option('Settings', 'option_to_delete', 'value')

    # Create or update options for Database
    config_handler.create_or_update_option('Database', 'host', 'localhost')
    config_handler.create_or_update_option('Database', 'port', '3306')

    config_handler.create_or_update_option('Test', 'option', 'value')

    # Save changes to the config file
    config_handler.save_changes()

    # Create or update an option
    config_handler.create_or_update_option('Database', 'database_name', 'my_db')

    # Read all sections
    print("Sections:", config_handler.read_sections())

    # Read all options within a section
    print("Options in 'Settings':", config_handler.read_options('Settings'))

    # Read the value of an option
    print("Value of 'host' in 'Database':", config_handler.read_value('Database', 'host'))

    # Check if a section exists
    print("Does 'Settings' section exist?", config_handler.check_section_exists('Settings'))

    # Check if an option exists within a section
    print("Does 'Database' section have 'port' option?", config_handler.check_option_exists('Database', 'port'))

    # Get all options with their corresponding values within a section
    print("Options with values in 'Settings':", config_handler.get_all_options_with_values('Settings'))

    # Delete an option
    config_handler.delete_option('Settings', 'option_to_delete')

    # Delete a section
    config_handler.delete_section('Test')

    # Rename a section
    config_handler.rename_section('Settings', 'SystemSettings')

    # Clear a section
    # config_handler.clear_section('SystemSettings')

    # Save changes to the config file
    config_handler.save_changes()

    manager = RecentFilesManager('example.ini', num_of_files=5)

    # Add some recent files
    manager.add_file('/path/to/recent/file1.txt')
    manager.add_file('/path/to/recent/file2.txt')
    manager.add_file('/path/to/recent/file3.txt')
    recent_files = manager.get_recent_files()
    print("Recent Files:", recent_files)

    # Show reshuffle
    manager.add_file('/path/to/recent/file2.txt')
    recent_files = manager.get_recent_files()
    print("Recent Files:", recent_files)


if __name__ == "__main__":
    main()