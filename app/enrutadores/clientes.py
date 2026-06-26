from fastapi import APIRouter, HTTPException
from modelos.clientes import Cliente, ClienteCrear, ClienteEditar
from listas import lista_clientes, lista_facturas
from conexion_bd import Sesion_dependencia
from sqlmodel import select

rutas_clientes = APIRouter()
#lista_clientes: list[Cliente] =[]


#endpoint, para listar todos los clientes
@rutas_clientes.get("/clientes", response_model=list[Cliente])
async def obtener_clientes(sesion: Sesion_dependencia):
    lista_cli = sesion.exec(select(Cliente)).all()
    return lista_cli


#endpoint, para obtebe o listar un solo cliente de la lista
@rutas_clientes.get("/clientes/{cliente_id}", response_model=Cliente)
async def listar_cliente(cliente_id: int, mi_sesion: Sesion_dependencia):
    #recorrer la lista cliente
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:
            return obj_cliente
        raise HTTPException(status_code=400, detail=f"La cliente con id {cliente_id}no existe"
        )






#endpoint, para crear un cliente y agregar a la lista
@rutas_clientes.post("/clientes", response_model=Cliente)
async def crear_cliente(datos_cliente: ClienteCrear, mi_sesion: Sesion_dependencia):
    Cliente_val = Cliente(**datos_cliente.model_dump())
    mi_sesion.add(Cliente_val)
    mi_sesion.commit()
    mi_sesion.refresh(Cliente_val)
    return Cliente_val
# Clase: git checkout para separar commits

#endpoint, para editar un cliente y agregar a la lista
@rutas_clientes.patch("/clientes/{cliente_id}", response_model=Cliente)
async def editar_cliente(cliente_id: int, datos_cliente: ClienteEditar):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:
            #validar clientes
            Cliente_val = Cliente.model_validate(datos_cliente.model_dump())
            Cliente_val.id = cliente_id
            lista_clientes[1] = Cliente_val
            return Cliente_val
    raise HTTPException(
        status_code=400, detail=f"El cliente con id{cliente_id}, no existe"
                        )




#endpoint de eliminar cliente
@rutas_clientes.delete("/clientes/{cliente_id}", response_model=Cliente)
async def elimnar_cliente(cliente_id: int):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:
            cliente_eliminado = lista_clientes.pop(i)
            return cliente_eliminado
        raise HTTPException(
            status_code=400, detail=f"El cliente con id {cliente_id}, no existe"
        )