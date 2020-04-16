"""This singleton class handles the cache, maintains a single checksum store and handles outputting receipts in the expected format. It is designed so that no matter how many instances you have, you end up with the same cache instance (singleton)."""

import asyncio
import uuid
import json

from aiocache import caches, Cache
from loguru import logger


from .errors import *

caches.set_config({
    'default': {
        'cache': "aiocache.SimpleMemoryCache"
        }
    }
})



class Mempool:
    """wraps aiocache with serialization and threading abstracted from main server invocation file."""
    CHECKBACK=30    #set the time for clients to re-check timestamps (in seconds)
    def __init__(self, sub_block=0):
        self.cache = caches.get('default')   # This always returns the same instance
        self.block=sub_block

    async def add_with_reciept(self, bytestr):
        """adds the digest to the cache and gives a reciept. 
        
        Note: must be awaited

        Param: the digest to add to the cache, in bytes.

        Raises: ExistsInCacheError
        """
        req_id=uuid.uuid1()
        try:
            await self.cache.add(bytestr, req_id)
            logger.info("Checksum {} added to cache by request {}", bytestr, req_id)
            return json.dumps(
                            {"request": req_id,
                             "digest": bytestr,
                             "status": "ACCEPTED",
                             "checkback": Mempool.CHECKBACK 
                            })

        except ValueError:
            logger.info("Checksum {} exists in cache", bytestr)
            return ExistsInCacheError
        
    def exists(self, bytestr):
        return self.cache.exists(bystr)
