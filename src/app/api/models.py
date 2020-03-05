from pydantic import BaseModel, Json


class StampRequestSchema(BaseModel):
    transaction: Json

class TreeProofSchema(BaseModel):
    proof: Json
    
class ProofSchema(BaseModel):
    proof: Json