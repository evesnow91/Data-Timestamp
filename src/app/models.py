from typing import Any, Dict

from pydantic import BaseModel,BaseConfig, Json
from fastapi.encoders import jsonable_encoder
from pymerkle import Proof

"""pymerkle supports two kind of proofs - consistency and audit proofs. Consistency proofs demonstrate that a past recorded state is a definite ancestor to the current merkle root. Audit proofs submit a challenge (the 'timestamp') in order to validate it exists in the tree."""

class APIModel(BaseModel):
    class Config(BaseConfig):
        orm_mode = True

    def dump_obj(self, **jsonable_encoder_kwargs: Any) -> Dict[str, Any]:
        return jsonable_encoder(self, **jsonable_encoder_kwargs)



class StampProof():
    def __init__(self,proof):
    """Please pass proof as JSON"""        
    self.proof = proof

class TreeProof():
    proof: Proof

