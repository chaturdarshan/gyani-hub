class GyanniHubError(Exception):
    """Base exception class for Gyanni.Hub project."""

    def __init__(self, message="An error occurred in the Gyanni.Hub project."):
        self.message = message
        super().__init__(self.message)


class DatabaseError(GyanniHubError):
    """Exception raised for errors related to database operations."""

    def __init__(self, message="Error occurred during database operation."):
        super().__init__(message)


class AuthenticationError(GyanniHubError):
    """Exception raised for authentication errors."""

    def __init__(self, message="Authentication failed."):
        super().__init__(message)


class AuthorizationError(GyanniHubError):
    """Exception raised for authorization errors."""

    def __init__(self, message="You are not authorized to perform this action."):
        super().__init__(message)


class ValidationError(GyanniHubError):
    """Exception raised for validation errors."""

    def __init__(self, message="Validation failed."):
        super().__init__(message)
