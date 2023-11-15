from fastapi import FastAPI
from pydantic import BaseModel      #NOS PERMITE CREAR UNA ENTIDAD

app = FastAPI()



@app.get("/usersjson")
async def usersjson():
    return [{"name": "Nahuel", "surname":"Andujar", "url":"https://andujar.dev", "age": 24},
            {"name": "Martin", "surname":"Casillo", "url":"https://casillo.dev", "age": 23},
            {"name": "Gonzalo", "surname":"Yepes", "url":"https://yepes.com", "age":24}]
    
# ENTIDAD USER

class User (BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int
    
    
@app.get("/usersclass")
async def users():
    return user_list

user_list = [User(id=1, name="Nahuel", surname="Andujar",url="https://andujar.dev",age=24),
             User(id=2, name="Martin", surname="Casillo",url="https://casillo.dev",age=23),
             User(id=3, name="Gonzalo",surname= "Yepes",url="https://yepes.dev",age=24)]

@app.get("/users")
async def users():
    return user_list

#PATH
@app.get("/user/{id}")     #AL LLAMAR A /USERS NOS DEVUELVE EL PARAMETRO QUE LE PASEMOS, EN ESTE CASO {ID}
async def user(id:int):
    return search_user(id)
 
#QUERY
@app.get("/userquery/")     #EN LA URL TENEMOS QUE PONER EL PARAMETRO, QUEDANDO URL/?ID=X  
async def user(id: int):
    return search_user(id)  

@app.post("/user/")     #FORMA DE AGREGAR DATOS
async def user(user: User):
    if type(search_user(user.id)) == User:  #COMPRUEBA SI EL ID YA EXISTE, SI NO LO AGREGA A LA LISTA DE USUARIOS
        return {"error":"El usuario ya existe"}
    else: 
        user_list.append(user)
        return user
        
@app.put ("/user/")     #FORMA DE MODIFICAR DATOS
async def user(user: User):
    found = False
    for index, saved_user in enumerate(user_list):
        if saved_user.id == user.id:
            user_list[index] = user
            found = True
    if not found:
        return {"error":"No se ha actualizado el usuario"}
    else:
        return user

@app.delete("/user/{id}")     #FORMA DE ELIMINAR UN USUARIO POR ID
async def user(id:int):
    found = False
    for index, saved_user in enumerate(user_list):
        if saved_user.id == id:
            del user_list[index]
            found = True
    if not found:
        return {"error":"No se ha eliminado el usuario"}
    else:
        return "Se elimino el usuario"
            

def search_user (id:int):       #FUNCION PARA BUSCAR USUARIOS POR ID CON QUERY
    users = filter(lambda user: user.id == id, user_list)   #ALMACENAMOS EN UNA VARIABLE UNA FUNCION QUE BUSCA COINCIDENCIA ENTRE EL ID QUE PASAMOS Y EL ID DE USUARIO DENTRO DE LA LISTA
    try:
        return list(users)[0]   #SI EL ID COINCIDE, MUESTRA EL USUARIO
    except:
        return {"error":"No se ha encontrado el usuario"}   #SI EL ID NO COINCIDE DA UN JSON CON UN MENSAJE DE ERROR


