from fastapi import Request, Response

from mlserver.model import MLModel
from mlserver.handlers import custom_handler

from . import default_logger


class PayloadTransformerRuntime(MLModel):
    """
    """

    @custom_handler(rest_path="/")
    async def invocations(self, request: Request) -> Response:
        """
        """
        return await default_logger.index(request)
