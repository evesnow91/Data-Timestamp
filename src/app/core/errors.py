# errors
import fastapi_jsonrpc as jsonrpc

class DigestFormatError(jsonrpc.BaseError):
    CODE = 6000
    MESSAGE = 'Digest improperly formed error'

class ValidationError(jsonrpc.BaseError):
    CODE = 6001
    MESSAGE = 'The proof could not be validated'


class DigestNotFoundError(jsonrpc.BaseError):
    CODE = 6002
    MESSAGE = 'Digest is not in the merkle tree'

