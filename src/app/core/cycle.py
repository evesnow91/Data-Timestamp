""" This singleton handles the waiting and firing of events to tightly-integrate the calendar to the Zilliqa block minting process.

It assumes:

 - The ZILLIQA_NETWORK env variable is set.
 - The RPC is up, addressable.
 - The Account set in ZILLIQA_PKEY env variable has sufficient funds.
 """

 