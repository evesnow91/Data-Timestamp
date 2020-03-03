from fastapi import FastAPI

from app.api import stamp, tree
from app.log import LogHandler


app = FastAPI()
merkle_tree = tree();
 
# configure database safety
@app.on_event("startup")
async def startup():
    connection = handle.open()
    database = connection.root


@app.on_event("shutdown")
async def shutdown():
    await handle.close()


app.include_router(stamp.router, prefix="/stamp")
app.include_router(tree.router, prefix="/tree", tags=["tree"])