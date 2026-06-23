from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

#Crear modelo clientes (id, nombre, email, descripcion)
class Cliente(BaseModel):
    id: int
    nombre: str
    email: str
    descripcion: str


listar_clientes: list[Cliente]= []


#endpoint, para listar todos los clientes
@app.get("/clientes")
def obtener_clientes():
    return listar_clientes

#endpoint, para obtebe o listar un solo cliente de la lista
@app.get("/clientes/{cliente_id}")
def listar_cliente(cliente_id: int):
    #recorrer la lista cliente
    for i, obj_cliente in enumerate(listar_clientes):
        if obj_cliente.get("id") == cliente_id:
            return obj_cliente

#endpoint, para crear un cliente y agregar a la lista
@app.post("/clientes")
def crear_cliente(datos_cliente: Cliente):
    listar_clientes.append(datos_cliente)
    return datos_cliente
