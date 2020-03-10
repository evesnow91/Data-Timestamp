from pydantic import BaseModel, Json
"""pymerkle supports two kind of proofs - consistency and audit proofs. Consistency proofs demonstrate that a past recorded state is a definite ancestor to the current merkle root. Audit proofs submit a challenge (the 'timestamp') in order to validate it exists in the tree."""

class StampProofSchema(BaseModel):
    proof: Json

class TreeProofSchema(BaseModel):
    proof: Json
    