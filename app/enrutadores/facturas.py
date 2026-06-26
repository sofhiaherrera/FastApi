from fastapi import APIRouter, HTTPException, status
from modelos.facturas import Factura, FacturaCrear, FacturaEditar
from modelos.clientes import Cliente
from listas import lista_facturas, lista_clientes
from conexion_bd import Sesion_dependencia
from sqlmodel import select

rutas_facturas =APIRouter()

#lista_clientes: list[Cliente] = []
#lista_facturas: list[Factura] = []


@rutas_facturas.get("/facturas", response_model=list[Factura])
async def listar_facturas(sesion: Sesion_dependencia):
    #select * from factura
    consulta = select(Factura)
    lista_facturas = sesion.exec(consulta).all()
    return lista_facturas


@rutas_facturas.get("/facturas/{factura_id}", response_model= Factura)
async def listar_factura(factura_id: int):
    #recorrer la lista de facturas
    for i, obj_factura in enumerate(lista_facturas):
        if obj_factura.id == factura_id:
            return obj_factura
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=f"La factura con id {factura_id}no existe"
    )



@rutas_facturas.post("/facturas/{cliente_id}", response_model= Factura)
async def crear_factura(cliente_id: int, datos_factura: FacturaCrear, sesion: Sesion_dependencia):
    #buscar el cliente en bd

    cliente_encontrado = sesion.get(Cliente, cliente_id) 
    #mensaje si no existe el cliente
    if not cliente_encontrado:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"El cliente con id {cliente_id}, no existe"
        )
    

    #validar datos de factura-json, pasar dict
    factura_dict = datos_factura.model_dump()
    factura_dict["cliente_id"] = cliente_id
    factura_val = Factura.model_validate(factura_dict)
    
    #guardar en bd
    sesion.add(factura_val)
    sesion.commit()
    sesion.refresh(factura_val)
    return factura_val

#
@rutas_facturas.patch("/facturas/{id_factura}", response_model= Factura)
async def editar_factura(id_factura: int, datos_factura: FacturaEditar):
    pass


@rutas_facturas.delete("/facturas/{id_factura}", response_model= Factura)
async def eliminar_factura(id_factura):
    pass

