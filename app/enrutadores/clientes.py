from fastapi import APIRouter, HTTPException, status
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
@rutas_clientes.get(
        "/clientes/{cliente_id}", 
        response_model=Cliente
)
async def listar_cliente(cliente_id: int, mi_sesion: Sesion_dependencia):
    cliente_bd = mi_sesion.get(Cliente, cliente_id)
    if not cliente_bd:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"El cliente con id {cliente_id}, no existe"
        )
        return cliente_bd


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
async def editar_cliente(
    cliente_id: int, datos_cliente: ClienteEditar, mi_sesion: Sesion_dependencia
):
    cliente_bd = mi_sesion.get(Cliente, cliente_id)
    if not cliente_bd:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
              detail=f"El cliente con id {cliente_id}, no existe"
        )
    cliente_dict = datos_cliente.model_dump(exclude_unset=True)
    cliente_bd.sqlmodel_update(cliente_dict)
    mi_sesion.add(cliente_bd)
    mi_sesion.commit()
    mi_sesion.refresh(cliente_bd)
    return cliente_bd


#endpoint de eliminar cliente
@rutas_clientes.delete("/clientes/{cliente_id}", response_model=Cliente)
async def elimnar_cliente(cliente_id: int, mi_sesion: Sesion_dependencia):
    cliente_bd = mi_sesion.get(Cliente, cliente_id)
    if not cliente_bd:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
              detail=f"El cliente con id {cliente_id}, no existe"
        )
    mi_sesion.delete(cliente_bd)
    mi_sesion.commit()
    #retornar un mensaje, deben quitar el response_model
    return cliente_bd