import json
import os

def write_content(workingDir, CPFormat, config, changes):
    confSchema = {}

    for configName, configAllowValues, configDefault in config:
        confSchema[configName] = {
            "AllowValues": configAllowValues,
            "Default": configDefault
        }

    uhhChanges = [] # Think of better name

    for action, fromFile in changes:
        uhhChanges.append({
            "Action": action,
            "FromFile": fromFile
        })

    data = {
        "$schema": "https://smapi.io/schemas/content-patcher.json",
        "Format": CPFormat,  
        "ConfigSchema": confSchema,
        "Changes": uhhChanges,
    }

    os.makedirs(workingDir, exist_ok=True)
    with open(workingDir + "content.json", "w") as f:
        json.dump(data, f, indent="\t")

