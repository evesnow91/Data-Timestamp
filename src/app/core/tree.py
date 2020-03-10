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

    def add(self, digest):
        """adds the given digest to the merkle tree"""
        self.merkle.encryptRecord(digest)

    def proof_from(self, digest):
        """This function gets the proof of existance from the tree for this given digest. If it is a novel digest, the timestamp proof is newly minted. Otherwise a valid upgrade proof is given for that digest.

        Assumes that the digest is hexadecimal.
                
        Returns:
        the challenge needed to fetch a full proof from the merkle tree"""
        self.merkle.encryptRecord(self, digest)

        # note this function assumes hexadecimal.
        return self.merkle.merkleProof()
