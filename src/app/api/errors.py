# errors
import fastapi_jsonrpc as jsonrpc

class DigestFormatError(jsonrpc.BaseError):
    CODE = 6000
    MESSAGE = 'Digest improperly formed error'

