from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from utils.load_to_file import *

NAMES_PATH = "data/names.txt"

app = FastAPI()

@app.get("/test/")
def test():
    return {"msg":"hi from test"}


@app.get("/test/")
def add_name(name:str):
    names_list = load_data(NAMES_PATH)
    names_list.append(name)
    save_data(names_list, NAMES_PATH)
    return {"msg": "saved user"}


class Caesar(BaseModel):
    text:str
    offeset: int
    mode: str


@app.post("/caesar/")
def caesar_encrypt(body:Caesar):
    if body.mode != "encrypt" or body.mode != "decrypt":
        HTTPException(status_code=500, detail="Please enter encryption or decryption.")
    text = body.text.lower() 
    encrypt_test = ""
    offeset = body.offeset
    letter_range = 122 - offeset
    for i in range(len(text)):
        if ord(text[i]) < letter_range:
            asc_letter = ord(text[i]) + body.offeset
            encrypt_test += chr(asc_letter)
        else:
            asc_letter = ord(text[i]) % letter_range + 96
            encrypt_test += chr(asc_letter)
    return {body.mode: encrypt_test}


@app.get("/fence/encrypt/")
def fence_encrypt(text:str):
    text = text.split(" ")
    text = "".join(text)
    encrypt_text = ""
    for i in range(0, len(text), 2):
        encrypt_text += text[i]
    for i in range(1, len(text), 2):
        encrypt_text += text[i]
    return {"encrypt_text": encrypt_text}

class Fence(BaseModel):
    text: str


@app.post("/fence/decrypt/")
def fence_decrypt(text: Fence):
    text = text.text
    decrypt_text = text[0]
    miidle = text // 2 - 1
    for i in range(1, len(text)):
        if i % 2 == 0:
            decrypt_text += text[i]
        else:
            decrypt_text += text[miidle + i]
    return {"decrypt": decrypt_text}




if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)