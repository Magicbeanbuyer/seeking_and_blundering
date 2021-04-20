"""Read lastpass secrets via its API."""
import os

import lastpass


class LastPassManager:
    """LastPass functions."""

    def __init__(self):
        """Instantiate a lastpass client."""
        self.user = None
        self.password = None
        self.vault = None

    def connect(self, user: str, password: str = None):
        """Connect to LastPass account.

        Args:
            user (str): User for LastPass account
            password (str): Password for LastPass account

        Returns:
            bool: True or False

        """
        self.user = user
        self.password = password
        self.vault = lastpass.Vault.open_remote(user, password)

    def get_accounts(self) -> list:
        """Get all passwords from LastPass account.

        Returns:
            list: Every list item includes numerator dictionary with all password fields

        """
        accounts = []
        for i in self.vault.accounts:
            accounts.append(
                {
                    "id": str(i.id, "utf-8"),
                    "name": str(i.name, "utf-8"),
                    "username": str(i.username, "utf-8"),
                    "password": str(i.password, "utf-8"),
                    "url": str(i.url, "utf-8"),
                    "group": str(i.group, "utf-8"),
                    "notes": str(i.notes, "utf-8"),
                }
            )
        return accounts


user_name = "xxx"
password = os.getenv("LASTPASS_PASSWORD")
my_lp_client = LastPassManager()
my_lp_client.connect(user_name, password)
ll = my_lp_client.get_accounts()
print(len(ll))
