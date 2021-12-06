"""
converter arquivos para json
"""

import json

d1 = {
    "pessoa 1": {
        "nome": "Anderson",
        "idade": 30,
    },
        "pessoa 2": {
        "nome": "Anderson",
        "idade": 30,
    }
}

d1_jsaon = json.dumps(d1)

with open("arquivo.json", "w+") as file:


    print(d1)