import requests
import json

# -------------------------
# Jinja2
# -------------------------
from jinja2 import Environment, FileSystemLoader
template_dir = 'Templates/'
env = Environment(loader=FileSystemLoader(template_dir))
ipFabric_template = env.get_template('ipfabric.j2')


# -------------------------
# Headers
# -------------------------
token = "YOUR TOKEN HERE"
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'X-API-Token': f'{ token }'
  }

# -------------------------
# All Countries
# -------------------------
allSnapshots = requests.request("GET", "https://demo8.ipfabric.io/api/v1/snapshots", headers=headers)
allSnapshotsJSON = allSnapshots.json()

parsed_all_output = ipFabric_template.render(allSnapshots = allSnapshotsJSON)

with open("IPFabric.md", "w") as fh:
    fh.write(parsed_all_output)               
    fh.close()