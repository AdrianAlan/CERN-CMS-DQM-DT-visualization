class UrlError(Exception):
    def __init__(self, message):
        super().__init__(message)

class ValidationError(Exception):
    def __init__(self, message):
        super().__init__(message)

class FetchError(Exception):
    def __init__(self, message):
        super().__init__(message)

class ConfigError(Exception):
    def __init__(self, message):
        super().__init__(message)

class NotSingleResultError(Exception):
    def __init__(self, message):
        super().__init__(message)