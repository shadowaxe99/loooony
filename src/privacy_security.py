```python
from src.models.user import User
from src.constants import PRIVACY_SECURITY

class PrivacySecurity:
    def __init__(self, user: User):
        self.user = user

    def update_privacy_settings(self, settings: dict):
        """
        Update user's privacy settings
        """
        self.user.privacy_settings = settings
        self.user.save()

    def update_security_settings(self, settings: dict):
        """
        Update user's security settings
        """
        self.user.security_settings = settings
        self.user.save()

    def get_privacy_settings(self):
        """
        Get user's privacy settings
        """
        return self.user.privacy_settings

    def get_security_settings(self):
        """
        Get user's security settings
        """
        return self.user.security_settings

    def check_privacy_compliance(self, data: dict):
        """
        Check if data complies with user's privacy settings
        """
        for key, value in data.items():
            if key in self.user.privacy_settings and not self.user.privacy_settings[key]:
                return False
        return True

    def check_security_compliance(self, data: dict):
        """
        Check if data complies with user's security settings
        """
        for key, value in data.items():
            if key in self.user.security_settings and not self.user.security_settings[key]:
                return False
        return True
```