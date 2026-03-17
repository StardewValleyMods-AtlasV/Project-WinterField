import json
import os

from manifest import write_manifest
from maps import write_maps
from content import write_content


rootDir = "/mnt/Coding/Coding/Stardew Mods/Project-WinterField/"
workingDir = rootDir + "[CP] WF/"
CPFormat = "2.9.0"

manifest = {
    "name": "Project WinterField",
    "version": "0.0.1",
    "description": "a test description",
    "UniqueID": "AtlasV.ProjectWinterField",
    "dependencies": [
        ["kittycatcasey.Stardew3D", True],
    ]
}

# "configName", "configAllowValues", "configDefault"
config = [
]

# "MapFileWithExtension", "ArrivalTileX", "ArrivalTileY"
maps = [
    ("TemplateWinterField.tmx", 10, 18),
]

# "Action", "FromFile"
changes = [
    ("Include", "Assets/Maps/maps.json"),
]

write_manifest(workingDir, **manifest)
write_maps(workingDir, maps)

write_content(workingDir, CPFormat, config, changes)
# ZipIt(stuff)