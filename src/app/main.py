import fastapi_jsonrpc as jsonrpc
from fastapi import Depends
from loguru import logger

from core.tree import *
from core.errors import *


# import models
# JSON-RPC entrypoint

api_v1 = jsonrpc.Entrypoint('/api/v1/')

merkle_tree = Tree();
# logger = log();
 

# RPC Methods

# DEPRECATED: INSTEAD GET MERKLE ROOT FROM ZILLIQA
# @api_v1.method()
# def root():
#     return merkle_tree.current_root()

@api_v1.method(errors=[DigestFormatError])
def stamp(digest:bytes) -> str:
    """The response will be a new proof, or an existing proof upgraded to its latest commitment.""" 
    return merkle_tree.stamp(digest)


@api_v1.method()
def consistency(past_root:str) -> str:
    """This method calls the merkle tree's consistency proof - demonstrating a given merkle root is an ancestor of the present one. If nothing is passed as parameter, the present merkle root is returned."""
    return merkle_tree.consistency_proof(past_root)


@api_v1.method()
def validate(proof:str) -> str:
    """This method validates the serialized proof against its local merkle tree. It does not indicate that the proof is anchored, only that its digest exists and the proof is well-formed."""
    return merkle_tree.validate(proof)


# entrypoint: ./api/v1/... methods=stamp, tree, validate
app = jsonrpc.API()
app.bind_entrypoint(api_v1)


# configure logger session
@app.on_event("startup")
async def startup():
    pass

# Dump the logs if a shutdown is occuring.
@app.on_event("shutdown")
async def shutdown():
    # ideally you'd put this backup in a docker volume, S3 or Grafana-compatible store.
    merkle_tree.export('tree.json')

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', port=5000, debug=True, access_log=False)
