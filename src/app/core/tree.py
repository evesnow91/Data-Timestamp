"""This singleton class handles merkle tree interactions, maintains a single digest store and handles outputting proofs in the respective format. It may form the basis for a Zilliqa implementation of the [SideTree](https://github.com/decentralized-identity/sidetree/blob/master/docs/protocol.md) protocol as it is upgraded in the future."""

from pymerkle import *

class Tree:
    """Tree class wraps and uses the defaults for pymerkle. It accepts SHA-256 hashes, and UTF-8 encoding. For testing you might benefit from turning off preimage protection"""
    def __init__(self, file=None):
        """sets up the underlying merkle tree
        
        Parameters:
        file (str): Optional recovery of tree state dumped by export().
        """
        if file is None:
            self.merkle = MerkleTree()
        else:
            self.merkle = MerkleTree.loadFromFile(file)


    def export(self, file):
        self.merkle.export(file)