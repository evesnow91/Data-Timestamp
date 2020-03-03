""" This class wraps a pymerkle instance in order to add the needed features for outputting proofs that contain the necessary data to validate on-chain.
"""
from app.api.models import StampRequestSchema
from fastapi import APIRouter, HTTPException, Path
from pymerkle import *

router = APIRouter()

@router.get("/", response_model=ProofSchema)
async def read_all_pending_stamps():
    #TODO: return a merkle tree consistency proof
    pass
