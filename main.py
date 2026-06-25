from fastapi import FastAPI, HTTPException, status
from modelos.clientes import ClienteBase, ClienteCrear, Cliente, ClienteEditar
from modelos.facturas import Factura, FacturaBase, FacturaCrear, FacturaEditar
from modelos.transacciones import Transaccion, TransaccionBase, TransaccionCrear, TransaccionEditar

app = FastAPI()


listar_clientes: list[Cliente]= []
lista_facturas: list[FacturaBase]= []
lista_transacciones: list[TransaccionBase]= []


#endpoint, para listar todos los clientes
@app.get("/clientes", response_model=list[Cliente])
async def obtener_clientes():
    return listar_clientes


#endpoint, para obtebe o listar un solo cliente de la lista
@app.get("/clientes/{cliente_id}", response_model=Cliente)
async def listar_cliente(cliente_id: int):
    #recorrer la lista cliente
    for i, obj_cliente in enumerate(listar_clientes):
        if obj_cliente.id == cliente_id:
            return obj_cliente
        raise HTTPException(status_code=400, detail=f"La cliente con id {factura_id}no existe"
        )


#endpoint, para crear un cliente y agregar a la lista
@app.post("/clientes", response_model=Cliente)
async def crear_cliente(datos_cliente: ClienteCrear):
    Cliente_val = Cliente.model_validate(datos_cliente.model_dump())
    #generar id
    id_cliente = len(listar_clientes)+1
    Cliente_val.id =id_cliente
    listar_clientes.append(Cliente_val)
    return Cliente_val
# Clase: git checkout para separar commits
#endpoint, para editar un cliente y agregar a la lista
@app.patch("/clientes/{cliente_id}", response_model=Cliente)
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
@app.delete("/clientes/{cliente_id}", response_model=Cliente)
async def elimnar_cliente(cliente_id: int):
    for i, obj_cliente in enumerate(listar_clientes):
        if obj_cliente.id == cliente_id:
            cliente_eliminado = listar_clientes.pop(i)
            return cliente_eliminado
        raise HTTPException(
            status_code=400, detail=f"El cliente con id {cliente_id}, no existe"
        )
    


#crear los endpoint para facturas 


@app.get("/facturas", response_model=list[Factura])
async def listar_facturas():
    return lista_facturas


@app.get("/facturas/{factura_id}", response_model= Factura)
async def listar_factura(factura_id: int):
    #recorrer la lista de facturas
    for i, obj_factura in enumerate(lista_facturas):
        if obj_factura.id == factura_id:
            return obj_factura
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                         detail=f"La factura con id {factura_id}no existe"
        )



@app.post("/facturas/{cliente_id}", response_model= Factura)
async def crear_factura(cliente_id: int, datos_factura: FacturaCrear):
    #buscar el cliente
    cliente_encontrado = None 
    for cliente in listar_clientes:
        if cliente.id == cliente_id:
            cliente_encontrado = cliente
    #mensaje si no existe el cliente
    if not cliente_encontrado:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"El cliente con id {cliente_id}, no existe"
        )
    
    #validar datos de factura
    factura_val = Factura.model_validate(datos_factura.model_dump())
    factura_val.cliente = cliente_encontrado
    #id de la factura
    factura_val.id = len(lista_facturas)+1
    datos_factura.cliente = cliente_encontrado
    return factura_val

@app.patch("/facturas/{id_factura}", response_model= Factura)
async def editar_factura(id_factura: int, datos_factura: FacturaEditar):
    pass


@app.delete("/facturas/{id_factura}", response_model= Factura)
async def eliminar_factura(id_factura):
    pass



#Crear los endpoint para transaccion


@app.get("/transacciones", response_model=list [Transaccion])
async def listar_transacciones():
    pass


@app.get("/transacciones/{id_transaccion}", response_model= Transaccion)
async def listar_transaccion(id_transaccion: int):
    pass


@app.post("/transacciones/{id_factura}", response_model= Transaccion)
async def crear_transaccion(id_factura: int, datos_transaccion: Transaccion):
    pass 


@app.patch("/transacciones/{id_transaccion}", response_model= Transaccion)
async def editar_transaccion(id_transaccion: int, datos_transaccion: Transaccion):
    pass


@app.delete("/transacciones/{id_transaccion}", response_model= Transaccion)
async def eliminar_transaccion(id_transaccion: int):
    pass