from tinydb import TinyDB, Query


class Mempool:
    """This class caches digests until the service signals they've been added to the merkle tree. The cache is dumped every time the merkle root is added to the mainchain by convention. You might wish to validate your tree against the cache in testing."""

    def __init__(self, db_path):
        self.store = TinyDB(db_path)

    def add(self, UUID, digest: bytes):
        self.store.insert({"UUID": UUID, "digest": digest})
