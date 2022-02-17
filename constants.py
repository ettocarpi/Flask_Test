import json 
with open("/root/test_api/config.json", "r") as jsonfile:
    cfg = json.load(jsonfile)

logfile = cfg['logfile']

LOG_PATH = cfg['logfile']['path']
LOG_FORMAT = cfg['logfile']['format']