import fastapi_jsonrpc as jsonrpc
from fastapi import Depends
from pydantic import json
from core import *
from errors import *
# import models
# JSON-RPC entrypoint

api_v1 = jsonrpc.Entrypoint('/api/v1/')

merkle_tree = Tree();
cache = Cache('./cache.json');
# logger = log();
 

# RPC Methods
# @api_v1.method()
# def root():
#     return merkle_tree.current_root()

@api_v1.method(errors=[DigestFormatError])
def stamp(digest:bytes) -> json:
    """Due to the nature of Merkle proofs, only one method for interacting with digests is necessary - if a client wishes to submit a new digest, they only need to call this method with a novel digest. The response will either be a new proof, or an existing proof upgraded to its latest categorization.""" 
    return models.StampProofmerkle_tree.proof_from(digest)

@api_v1.method()
def consistency(past_root:str) -> json:
    """This method calls the merkle tree's consistency proof - demonstrating a given merkle root is an ancestor of the present one. If nothing is passed as parameter, the present merkle root is returned."""
    return merkle_tree.consistency_proof(past_root)



# entrypoint: ./proof methods=stamp, tree
app = jsonrpc.API()
app.bind_entrypoint(api_v1)


# configure database safety
@app.on_event("startup")
async def startup():
    pass

# Dump the logs if a shutdown is occuring.
@app.on_event("shutdown")
async def shutdown():
    pass

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', port=5000, debug=True, access_log=False)
