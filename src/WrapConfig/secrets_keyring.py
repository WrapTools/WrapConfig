# # secrets.py
#
# import logging
# import configparser
# from pathlib import Path
#
# logger = logging.getLogger(__name__)
#
#
# # NOT YET IMPLMENTED AN TESTED
# import keyring
# from keyring.errors import PasswordDeleteError
#
# class KeyringSecretsManager:
#     """
#     A lightweight manager that uses the 'keyring' library to store/retrieve/delete secrets
#     in the user's OS-specific credential manager (Windows Credential Manager,
#     macOS Keychain, or Linux Secret Service).
#     """
#     def __init__(self, service_name="MyApp"):
#         """
#         :param service_name: Identifies your application within the OS keyring.
#         """
#         self.service_name = service_name
#
#     def set_secret(self, key: str, value: str) -> None:
#         """
#         Store a secret (e.g. API key) in the OS keyring.
#         """
#         keyring.set_password(self.service_name, key, value)
#
#     def get_secret(self, key: str) -> str | None:
#         """
#         Retrieve a secret from the OS keyring. Returns None if not found.
#         """
#         return keyring.get_password(self.service_name, key)
#
#     def delete_secret(self, key: str) -> None:
#         """
#         Delete a secret from the OS keyring.
#         If the secret doesn't exist, it won't raise an error.
#         """
#         try:
#             keyring.delete_password(self.service_name, key)
#         except PasswordDeleteError:
#             # Password was not found or couldn't be deleted
#             pass
