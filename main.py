from fastapi import FastAPI
# from typing_extensions import TypedDict
# from typing import List
# from data import wakil_rakyat_parlimen
import json

# from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to Wakil Rakyat API! Go to /docs for more information."}


"""
Ahli Parlimen:

{
    id: 1,
    kod: "P0001",
    pru: 14,
    kawasan: "Padang Besar",
    nama_wakil_rakyat: "Zahidi bin Zainul Abidin",
    parti: "BN - UMNO",
    negeri: "Perlis",
    dun: [
        {
        ....
        }
    ]
}
"""
"""
ADUN:

{
    id: 1,
    kod: "P0001",
    pru: 14,
    kawasan: "Padang Besar",
    nama_wakil_rakyat: "Zahidi bin Zainul Abidin",
    parti: "BN - UMNO",
    negeri: "Perlis",
    parlimen: 32
}

/pru/14/negeri/selangor/dun/21
/pru/13/parlimen/33

/parlimen/93/dun/2

parlimen = {
    id: 1,
    kod: "P001",
    kawasan: "Padang Besar",
    nama_wakil_rakyat: "Zahidi bin Zainul Abidin",
    parti: "BN - UMNO",
    negeri: "Perlis",
    dun: [
        {
            id: 1,
            kod: "N01",
            kawasan: "Padang Besar",
            nama_wakil_rakyat: "Zahidi bin Zainul Abidin",
            parti: "BN - UMNO",
            negeri: "Perlis",
        }
    ]
}

"""


# class WakilRakyat(BaseModel):
#     id: int
#     kod: str
#     kawasan: str
#     nama_wakil_rakyat: str
#     parti: str

# class WakilRakyat(TypedDict):
#     id: int
#     kod: str
#     kawasan: str
#     nama_wakil_rakyat: str
#     parti: str

# WakilRakyat = TypedDict(
#     "WakilRakyat",
#     {
#         "nombor_kod": int,
#         "kod": str,
#         "kawasan": str,
#         "nama_wakil_rakyat": str,
#         "parti": str
#     },
# )

# wakil_rakyat_parlimen_db: List[WakilRakyat] = wakil_rakyat_parlimen
with open('./data/clean/data.json') as json_file:
    wakil_rakyat_db = json.load(json_file)


@app.get("/parlimen")
async def all_ahli_parlimen():
    return wakil_rakyat_db


@app.get("/parlimen/{nombor_parlimen}")
async def parlimen(nombor_parlimen: int):
    if nombor_parlimen < 1 or nombor_parlimen > 222:
        return {"error": "Nombor kerusi parlimen tidak sah"}

    return [i for i in wakil_rakyat_db if i["nombor_kod"] == nombor_parlimen][0]


@app.get("/parlimen/{nombor_kerusi}/dun")
async def all_ahli_dun_by_parlimen(nombor_kerusi: int):
    if nombor_kerusi < 1 or nombor_kerusi > 222:
        return {"error": "Nombor kerusi parlimen tidak sah"}

    return [i for i in wakil_rakyat_db if i["nombor_kod"] == nombor_kerusi][0]["dun"]


@app.get("/parlimen/{nombor_parlimen}/dun/{nombor_dun}")
async def dun(nombor_parlimen: int, nombor_dun: int):
    if nombor_parlimen < 1 or nombor_parlimen > 222:
        return {"error": "Nombor kerusi parlimen tidak sah"}

    if nombor_dun < 1:
        return {"error": "Nombor kerusi DUN tidak sah"}

    duns = [i for i in wakil_rakyat_db if i["nombor_kod"] == nombor_parlimen][0]["dun"]

    dun = [i for i in duns if i["nombor_kod"] == nombor_dun]

    if len(dun) == 1:
        return dun[0]
    else:
        return {"error": "Nombor kerusi DUN tidak sah"}
