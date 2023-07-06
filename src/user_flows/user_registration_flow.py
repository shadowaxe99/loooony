```python
from src.user_registration import createUserAccount, recoverPassword
from src.constants import USER_DATA
from src.models.user import UserSchema

def user_registration_flow():
    # Open app and select "Create Account."
    createUserAccount()

    # Enter email, password, and required details.
    user_data = UserSchema().load(USER_DATA)

    # Complete registration via verification email.
    user_data.complete_registration()

    # Log in using credentials.
    user_data.login()

if __name__ == "__main__":
    user_registration_flow()
```