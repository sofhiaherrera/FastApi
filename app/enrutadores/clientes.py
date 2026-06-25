from fastapi import APIRouter, HTTPException
from..modelos.clientes import Cliente, ClienteCrear, ClienteEditar

rutas_clientes = APIRouter()
listar_clientes: list[Cliente]


#endpoint, para listar todos los clientes
@rutas_clientes.get("/clientes", response_model=list[Cliente])
async def obtener_clientes():
    return listar_clientes


#endpoint, para obtebe o listar un solo cliente de la lista
@rutas_clientes.get("/clientes/{cliente_id}", response_model=Cliente)
async def listar_cliente(cliente_id: int):
    #recorrer la lista cliente
    for i, obj_cliente in enumerate(listar_clientes):
        if obj_cliente.id == cliente_id:
            return obj_cliente
        raise HTTPException(status_code=400, detail=f"La cliente con id {factura_id}no existe"
        )


#endpoint, para crear un cliente y agregar a la lista
@rutas_clientes.post("/clientes", response_model=Cliente)
async def crear_cliente(datos_cliente: ClienteCrear):
    Cliente_val = Cliente.model_validate(datos_cliente.model_dump())
    #generar id
    id_cliente = len(listar_clientes)+1
    Cliente_val.id =id_cliente
    listar_clientes.append(Cliente_val)
    return Cliente_val
# Clase: git checkout para separar commits
#endpoint, para editar un cliente y agregar a la lista
@rutas_clientes.patch("/clientes/{cliente_id}", response_model=Cliente)
async def editar_cliente(cliente_id: int, datos_cliente: ClienteEditar):
    for i, obj_cliente in enumerate(listar_clientes):
        if obj_cliente.id == cliente_id:
            #validar clientes
            Cliente_val = Cliente.model_validate(datos_cliente.model_dump())
            Cliente_val.id = cliente_id
            listar_clientes[1] = Cliente_val
            return Cliente_val
    raise HTTPException(
        status_code=400, detail=f"El cliente con id{cliente_id}, no existe"
                        )




#endpoint de eliminar cliente
@rutas_clientes.delete("/clientes/{cliente_id}", response_model=Cliente)
async def elimnar_cliente(cliente_id: int):
    for i, obj_cliente in enumerate(listar_clientes):
        if obj_cliente.id == cliente_id:
            cliente_eliminado = listar_clientes.pop(i)
            return cliente_eliminado
        raise HTTPException(
            status_code=400, detail=f"El cliente con id {cliente_id}, no existe"
        )