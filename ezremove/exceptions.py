class EzRemoveError(Exception):
    """Base error for EzRemove SDK"""
    pass

class APIError(EzRemoveError):
    """Raised when the API returns an error code"""
    pass

class TimeoutError(EzRemoveError):
    """Raised when polling exceeds the time limit"""
    pass

class FileError(EzRemoveError):
    """Raised when there is an issue with the image file"""
    pass

