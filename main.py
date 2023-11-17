from fastapi import FastAPI
from routers import products, users
from fastapi.staticfiles import StaticFiles
app = FastAPI()

#ROUTERS
app.include_router(products.router)
app.include_router(users.router)
app.mount("/static",StaticFiles(directory="static"), name="static")

@app.get("/")       #Get signicia que se le enviamos algo al servidor indicado dentro del parentesis ("")
async def root ():      #async es para ejecutar una funcion sin esperar la respuesta del servidor
    return "¡Hello, FastAPI!"

#HAY QUE ACTIVAR EL SERVIDOR LOCAL CON uvicorn nombre_del_archivo:nombre_de_la_funcion --reload.
#EN ESTE CASO ES uvicorn main:app --reload 

@app.get("/url")
async def url():
    return {"url_curso":"https://moredev.com/python"}    #http://127.0.0.1:8000/url

#http://127.0.0.1:8000/docs#/ PARA VER LA DOCUMENTACION ACTUALIZADA AL MOMENTO      