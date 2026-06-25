from fastapi import FastAPI, HTTPException
from modelos.clientes import ClienteBase, ClienteCrear, Cliente, ClienteEditar
from modelos. facturas import Factura, FacturaCrear, FacturaEditar
from modelos.transacciones import Transaccion, TransaccionCrear, TransaccionEditar

app = FastAPI()


listar_clientes: list[Cliente]= []
lista_facturas: list[Factura]= []
lista_transacciones: list[Transaccion]= []


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


@app.get("/facturas/{id_factura}", response_model= Factura)
async def listar_factura(id_factura: int):
    pass


@app.post("/facturas/{id_cliente}", response_model= Factura)
async def crear_factura(id_cliente: int, datos_factura: Factura):
    pass 


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