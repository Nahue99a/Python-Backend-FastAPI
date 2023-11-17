from fastapi import APIRouter, HTTPException
from pydantic import BaseModel      #NOS PERMITE CREAR UNA ENTIDAD

router = APIRouter(prefix="/users",
                   tags=["users"],
                   responses={404: {"message":"No encontrado"}})



@router.get("/json")
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
    
    
@router.get("/class")
async def users():
    return user_list

user_list = [User(id=1, name="Nahuel", surname="Andujar",url="https://andujar.dev",age=24),
             User(id=2, name="Martin", surname="Casillo",url="https://casillo.dev",age=23),
             User(id=3, name="Gonzalo",surname= "Yepes",url="https://yepes.dev",age=24)]

@router.get("/")
async def users():
    return user_list

#PATH
@router.get("/{id}")     #AL LLAMAR A /USERS NOS DEVUELVE EL PARAMETRO QUE LE PASEMOS, EN ESTE CASO {ID}
async def user(id:int):
    return search_user(id)
 
#QUERY
@router.get("/query/")     #EN LA URL TENEMOS QUE PONER EL PARAMETRO, QUEDANDO URL/?ID=X  
async def user(id: int):
    return search_user(id)  

@router.post("/", response_model=User, status_code=201)     #FORMA DE AGREGAR DATOS.   STATUS_CODE = 201 DEVUELVE EL CODIGO 201 SI SE CREO UN USUARIO, response_model=User indicamos que tiene que devolver.
async def user(user: User):
    if type(search_user(user.id)) == User:  #COMPRUEBA SI EL ID YA EXISTE, SI NO LO AGREGA A LA LISTA DE USUARIOS
       raise HTTPException(status_code=404, detail="El usuario ya existe")  #SI EL ID EXISTE LANZA UN ERROR 204
    
    else: 
        user_list.append(user)
        return user
  
  
      
@router.put ("/", status_code=201)     #FORMA DE MODIFICAR DATOS
async def user(user: User):
    found = False
    for index, saved_user in enumerate(user_list):
        if saved_user.id == user.id:
            user_list[index] = user
            found = True
    if not found:
        raise HTTPException(status_code=406, detail= "No se ha actualizado el usuario, el ID no existe")
    else:
        return user


@router.delete("/{id}")     #FORMA DE ELIMINAR UN USUARIO POR ID
async def user(id:int):
    found = False
    for index, saved_user in enumerate(user_list):
        if saved_user.id == id:
            del user_list[index]
            found = True
    if not found:
        raise HTTPException(status_code=406, detail= "No se ha eliminado el usuario, el ID no existe")
    else:
        return "Se elimino el usuario"
            

def search_user (id:int):       #FUNCION PARA BUSCAR USUARIOS POR ID CON QUERY
    users = filter(lambda user: user.id == id, user_list)   #ALMACENAMOS EN UNA VARIABLE UNA FUNCION QUE BUSCA COINCIDENCIA ENTRE EL ID QUE PASAMOS Y EL ID DE USUARIO DENTRO DE LA LISTA
    try:
        return list(users)[0]   #SI EL ID COINCIDE, MUESTRA EL USUARIO
    except:
        return {"error":"No se ha encontrado el usuario"}   #SI EL ID NO COINCIDE DA UN JSON CON UN MENSAJE DE ERROR


