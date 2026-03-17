import json
import os

def write_manifest(workingDir, name, version, description, UniqueID, dependencies):

    data = {
        "$schema": "https://smapi.io/schemas/manifest.json",
        "Name": name,
        "Author": "AtlasV",
        "Version": version,
        "Description": description,
        "UniqueID": UniqueID,
        "ContentPackFor": {
            "UniqueID": "Pathoschild.ContentPatcher"
        },
        "Dependencies": [
            {
                "UniqueID": dep[0],
                "IsRequired": dep[1]
            }
            for dep in dependencies
        ],
    }

    os.makedirs(workingDir, exist_ok=True)
    with open(workingDir + "manifest.json", "w") as f:
        json.dump(data, f, indent="\t")

