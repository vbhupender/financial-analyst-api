
class InvalidTokenError(Exception):
    pass
class TokenNotFoundError(Exception):
    pass
class InvalidInputError(Exception):
    pass


class TokenValidator:
    def __init__(self, token_name):
        self.token_name = token_name
        self.available_token = ['AI_ENGINEER_2026']
        self.is_loaded = False

    def load_model(self):
        self.is_loaded = True
        print(f' {self.token_name} is Loaded')

    def verify_token(self, token):
        if self.token_name not in self.available_token:
            raise InvalidTokenError('Access Denied: Invalid Security Token')
        return f"Acess Granted"

engine = TokenValidator('guest_user')
engine.load_model()


try:
    print(' Starting Token Generation...')
    output = engine.verify_token(engine)
    print(output)

except InvalidTokenError as error:
    print(f' Alert: System security team notified! Error details: {error}')

except TokenNotFoundError as error:
    print(f"Updating Token Registry..:{error}")

except InvalidInputError as error:
    print(f'Wrong Input...: {error}')

except Exception as general_error:
    print(f'Caught an unexpected error:{general_error}')

else:
    print(" Token granted access successfully with zero issues")

finally:
    print('[CRITICAL] Code Executed.')
