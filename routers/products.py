from fastapi import APIRouter   #IMPORTAMOS APIRUTER PARA IMPORTAR LA BIBLIOTECA E INDICARLE AL ARCHIVO QUE NO VA A SER UNA API SINO UN ROUTER

router = APIRouter(prefix="/products",          #PREFIX = /PRODUCTS INDICA QUE TODOS LOS ROUTERS DENTRO DEL ARCHIVO SALEN DESDE PRODUCTS, NO HACE FALTA ESCRIBIRLO EN LA FUNCION DEVUELTA
                   tags = ["products"],         #TAGS = ["PRODUCTS"] INDICA QUE EN LA DOCUMENTACION AGRUPE TODO EL ARCHIVO EN EL TAG PRODUCTS
                   responses={404: {"message":"No encontrado"}})  

products_list = ["Producto 1", "Producto 2", "Producto 3", "Producto 4"]

@router.get("/")
async def products():
    return products_list

@router.get("/{id}")
async def products(id:int):
    return products_list[id]