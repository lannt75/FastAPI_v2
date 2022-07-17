from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from typing import Union


app = FastAPI()

@app.get("/")
def root():
    return {"Hello World"}

# API truyền parameter qua path
# app = FastAPI()
#
# @app.get("/items/")
# def read_item(name: str, address: str):
#     return [{"name": name}, {"address": address}]

# API truyền tham số bằng phương thức post qua request body, reponse file json
# class Infor(BaseModel):
#     name: str
#     address: str
#
# app = FastAPI()
#
# @app.post("/") #
# def create_item(infor: Infor):
#     return infor

# API truyền tham số qua request body + path parameter
# class Infor(BaseModel):
#     name: str
#     address: str
#
# app = FastAPI()
#
# @app.put("/infor/{infor_id}")
# async def create_infor(infor_id: int, infor: Infor):
#     return {"infor_id": infor_id, **infor.dict()}

# from fastapi import FastAPI, File, UploadFile, Request
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates
# import json
#
# app = FastAPI()
#
# templates = Jinja2Templates(directory="templates")
#
# @app.get("/infor", response_class=HTMLResponse) #response return là html
# def post(request=Request):
#     return templates.TemplateResponse("ex1.html", {"request": request})
#
# @app.post("/post")
# async def read(file: UploadFile = File(...)): #đọc file json được post lên
#     contents = await file.read()
#     data_submit = json.loads(contents.decode("utf-8"))
#
#     name = data_submit["name"]
#     address = data_submit["address"]
#     return name + address


