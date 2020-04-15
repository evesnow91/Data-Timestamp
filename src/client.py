"""This script has all the essential functions to access the timestamping functions of a Data-Timestamp calendar server."""
import hashlib
import requests

from jsonrpcclient.clients.http_client import HTTPClient
from jsonrpcclient.requests import Request

calendar_server="http://localhost:5000/api/v1/"

client = HTTPClient(calendar_server)
d
submit_request = Request("submit")
# calendar_server + "submit"
proof_request = calendar_server + "proof"
consistency_request = calendar_server + "consistency"

def stamp(digest):
    response = request(calendar_server, "submit"
    

if __name__ == '__main__':



# Submits a file by digest to the calendar server for timestamping. Caches the UUID response object to use later for requesting the proof

# Gets the Proof based on the UUID response

# Requests the corresponding root-update transaction to the viewblock api, validating that your calendar is anchored and your proof will be validated as long as the Zilliqa mainchain is reachable. 