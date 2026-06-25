from pydantic import BaseModel


#crear el modelo transaccion (id, cantidad, vr_unitaria, id_factura)
class TransaccionBase(BaseModel):
    cantidad: int
    vr_unitario: float
    factura_id: int 


class TransaccionCrear(TransaccionBase):
    pass


class TransaccionEditar(TransaccionBase):
    pass


class Transaccion(TransaccionBase):
    id: int | None = None
    #aqui va la relacion con el modelo cliente(solo un campo)