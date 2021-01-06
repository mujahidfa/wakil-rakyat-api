from fastapi import FastAPI
from typing_extensions import TypedDict
from typing import List
from data import wakil_rakyat_parlimen

# from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


"""
Ahli Parlimen:

{
    id: 1,
    kod: "P0001",
    kawasan: "Padang Besar",
    nama_wakil_rakyat: "Zahidi bin Zainul Abidin",
    gelaran: "YB Datuk",
    parti: "BN - UMNO",
    negeri: "Perlis",
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


WakilRakyat = TypedDict(
    "WakilRakyat",
    {"id": int, "kod": str, "kawasan": str, "nama_wakil_rakyat": str, "parti": str},
)

wakil_rakyat_parlimen_db: List[WakilRakyat] = wakil_rakyat_parlimen


@app.get("/kerusi")
async def kerusi_all():
    return wakil_rakyat_parlimen_db


@app.get("/kerusi/{nombor}")
async def kerusi(nombor: int):
    if nombor < 1 or nombor > 222:
        return {"message": "Nombor kerusi tidak sah"}

    return [i for i in wakil_rakyat_parlimen_db if i["id"] == nombor][0]
