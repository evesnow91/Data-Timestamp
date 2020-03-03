from app.api import crud
from app.api.models import StampRequestSchema
from fastapi import APIRouter, HTTPException, Path
from typing import List

router = APIRouter()
# No POST, because of how merkle tree proofs work.

@router.get("/{id}/", response_model=StampRequestSchema)
async def read_stamp(id: bytes):
    stamp = await crud.get(id)
    if not stamp:
        raise HTTPException(status_code=404, detail="stamp not found")
    return stamp

@router.get("/", response_model=List[NoteDB])
async def read_all_pending_stamps():
    return await crud.get_all_pending_stamps()

@router.put("/{id}/", response_model=NoteDB)
async def update_note(payload: NoteSchema, id: int = Path(..., gt=0),):
    note = await crud.get(id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    note_id = await crud.put(id, payload)

    response_object = {
        "id": note_id,
        "title": payload.title,
        "description": payload.description,
    }
    return response_object
