import json
import os

def write_maps(workingDir, maps):
    changes = []

    for unformattedName, X, Y in maps:
        name, fileExtension = unformattedName.rsplit(".", 1)

        modIDName = "{{ModId}}_" + name
        xy = f"{X}, {Y}"

        # EditData entry
        changes.append({
            "Action": "EditData",
            "Target": "Data/Locations",
            "Entries": {
                modIDName: {
                    "DisplayName": name,
                    "DefaultArrivalTile": xy,
                    "CreateOnLoad": {
                        "MapPath": "Maps/" + modIDName
                    },
                },
            }
        })

        # Load entry
        changes.append({
            "Action": "Load",
            "Target": "Maps/" + modIDName,
            "FromFile": "Assets/Maps/" + name + "." + fileExtension
        })

    data = {
        "$schema": "https://smapi.io/schemas/content-patcher.json",
        "Changes": changes
    }

    os.makedirs(workingDir + "Assets/Maps/", exist_ok=True)

    with open(workingDir + "Assets/Maps/maps.json", "w") as f:
        json.dump(data, f, indent=4)