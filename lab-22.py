import requests
import json
from requests.auth import HTTPBasicAuth

def eapi_request(device, commands):
    auth = HTTPBasicAuth("ntc", "ntc123")
    headers = {"Content-Type": "application/json"}
    url = f"http://{device}/command-api"
    payload = {
        "jsonrpc": "2.0",
        "method": "runCmds",
        "params": {
            "format": "json",
            "timestamps": False,
            "cmds": commands,
            "version": 1,
        },
        "id": "EapiExplorer-1",
    }
    response = requests.post(
        url, data=json.dumps(payload), headers=headers, auth=auth
    )
    return response

def get_eos_neighbors(response):
    data = json.loads(response.text)
    device_neighbors = data["result"][0]["lldpNeighbors"]
    neighbors_list = []
    for neighbor in device_neighbors:
        new_neighbor = {
            "neighbor_interface": neighbor["neighborPort"],
            "local_interface": neighbor["port"],
            "neighbor": neighbor["neighborDevice"],
        }
        neighbors_list.append(new_neighbor)
    return neighbors_list

def main():
    neighbors = {}
    devices = ["eos-spine1", "eos-spine2"]
    commands = ["show lldp neighbors"]
    for dev in devices:
        response = eapi_request(dev, commands)
        neighbors[dev] = get_eos_neighbors(response)
    print(json.dumps(neighbors, indent=4))

if __name__ == "__main__":
    main()
