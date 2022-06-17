import json
import uuid

addon_name = str(input("Addon name: "))
addon_desc = str(input("Addon description: "))
gametest_enabled = str(input("Gametest enabled ? type 'y' if yes or 'n' if not: "))
if gametest_enabled == "y":
  gametest_entry = str(input("entry file name: "))
  mojang_ui_enabled = str(input("mojang-minecraft-ui enabled ? type 'y' if yes or 'n' if not: "))
elif gametest_enabled == "n":
  gametest_entry = ""
  mojang_ui_enabled = "n"
else:
  gametest_entry = ""
  mojang_ui_enabled = "n"

manifest = {
  "format_version": 2,
  "header": {
    "description": addon_desc,
    "name": addon_name,
    "uuid": str(uuid.uuid4()),
    "version": [ 0, 0, 1 ],
    "min_engine_version": [ 1, 14, 0 ]
  },
  "modules": [],
  "dependencies": []
}

if gametest_enabled == "y":
  print("Gametest enabled")
  manifest["dependencies"] += [
    {
      "description": "mojang-gametest dependencie",
      "uuid": "b26a4d4c-afdf-4690-88f8-931846312678",
      "version": [ 0, 1, 0 ]
    },
    {
      "description": "mojang-minecraft dependencie",
      "uuid": "6f4b6893-1bb6-42fd-b458-7fa3d0c89616",
      "version": [ 0, 1, 0 ]
    }
  ]
  manifest["modules"] += [
    {
      "type": "data",
      "uuid": str(uuid.uuid4()),
      "version": [ 1, 0, 0 ]
    },
    {
      "description": "Javacript module",
      "type": "script",
      "language": "javascript",
      "uuid": str(uuid.uuid4()),
      "version": [ 0, 0, 1 ],
      "entry": str(f"scripts/{gametest_entry}")
    }
  ]    
elif gametest_enabled == "n":
  print("Gametest disabled")
else:
  print(f"Incorrect input for gametest option: {gametest_enabled}")
if mojang_ui_enabled == "y":
    manifest["dependencies"] += [
      {
        "description": "mojang-minecraft-ui dependencie",
        "uuid": "2bd50a27-aB5f-4f40-a596-3641627c635e",
        "version": [ 0, 1, 0 ]
      }
    ]
elif mojang_ui_enabled == "n":
  print("mojang-minecraft-ui disabled")  
else:
  print(f"Incorrect input for mojang-minecraft-ui option: {mojang_ui_enabled}")  

file = open("manifest.json", "x")
json.dump(manifest, file, indent=4)
input(f"Succesfully created a manifest\nADDON NAME: {addon_name}\nADDON DESCRIPTION: {addon_desc}\nGametest enabled: {'true' if gametest_enabled == 'y' else 'false'}\nmojang-minecraft-ui enabled: {'true' if mojang_ui_enabled == 'y' else 'false'}")
