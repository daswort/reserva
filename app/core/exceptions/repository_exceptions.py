class RepositoryError(Exception):
    """Excepción base para los errores del repositorio."""
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message

class CreateError(RepositoryError):
    """Error al crear un registro."""
    def __init__(self, detail: str = "Error al crear el registro en la base de datos."):
        super().__init__(detail)

class UpdateError(RepositoryError):
    """Error al actualizar un registro."""
    def __init__(self, detail: str = "Error al actualizar el registro en la base de datos."):
        super().__init__(detail)

class DeleteError(RepositoryError):
    """Error al eliminar un registro."""
    def __init__(self, detail: str = "Error al eliminar el registro en la base de datos."):
        super().__init__(detail)
