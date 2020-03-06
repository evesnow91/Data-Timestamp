from pydantic import BaseModel, Json


class StampProofSchema(BaseModel):
    proof: Json

class TreeProofSchema(BaseModel):
    proof: Json
    