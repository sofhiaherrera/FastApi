from fastapi import FastAPI, HTTPException
from modelos.clientes import ClienteBase, ClienteCrear

app = FastAPI()


listar_clientes: list[ClienteBase]= []


#endpoint, para listar todos los clientes
@app.get("/clientes", response_model=list[ClienteBase])
def obtener_clientes():
    return listar_clientes

#endpoint, para obtebe o listar un solo cliente de la lista
@app.get("/clientes/{cliente_id}", response_model=ClienteBase)
def listar_cliente(cliente_id: int):
    #recorrer la lista cliente
    for i, obj_cliente in enumerate(listar_clientes):
        if obj_cliente.get("id") == cliente_id:
            return obj_cliente

#endpoint, para crear un cliente y agregar a la lista
@app.post("/clientes", response_model=ClienteBase)
def crear_cliente(datos_cliente: ClienteCrear):
    ClienteBase_val = ClienteBase.model_validate(datos_cliente.model_dump())
    listar_clientes.append(ClienteBase_val)
    return ClienteBase_val
