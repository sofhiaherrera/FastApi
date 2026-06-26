from fastapi import APIRouter, HTTPException, status
from modelos.transacciones import Transaccion, TransaccionCrear, TransaccionEditar
from modelos.facturas import Factura
from listas import lista_transacciones, lista_facturas
from conexion_bd import Sesion_dependencia
from sqlmodel import select

rutas_transacciones = APIRouter()


#lista_factura: list[Factura] =[]
#lista_transacciones: list[Transaccion] = []


@rutas_transacciones.get("/transacciones", response_model=list [Transaccion])
async def listar_transacciones(sesion : Sesion_dependencia):
    #consulta = select(Transaccion)
    #lista_transacciones = sesion.exec(consulta).all()
    #return lista_transacciones
    return sesion.exec(select(Transaccion)).all()


@rutas_transacciones.get("/transacciones/{id_transaccion}", response_model= Transaccion)
async def listar_transaccion(id_transaccion: int):
    pass


@rutas_transacciones.post("/transacciones/{factura_id}", response_model= Transaccion)
async def crear_transaccion(
    factura_id: int, datos_transaccion: TransaccionCrear, sesion: Sesion_dependencia
):
    #buscar factura
    factura_encontrado = sesion.get(Factura, factura_id)
    #mensaje si no existe la factura
    if not factura_encontrado:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"La factura con id {factura_id}, no existe"
        )
    
    #validar datos de la transaccion json y pasaramos dict
    transaccion_dict = datos_transaccion.model_dump()
    transaccion_dict["Factura_id"] = factura_id
    transaccion_val = Transaccion.model_validate(transaccion_dict)
    #guardar en bd
    sesion.add(transaccion_val)
    sesion.commit()
    sesion.refresh(transaccion_val)
    return transaccion_val 


@rutas_transacciones.patch("/transacciones/{id_transaccion}")
async def editar_transaccion(id_transaccion: int, datos_transaccion: Transaccion):
    pass


@rutas_transacciones.delete("/transacciones/{id_transaccion}")
async def eliminar_transaccion(id_transaccion: int):
    pass