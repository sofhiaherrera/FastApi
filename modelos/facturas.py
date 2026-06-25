from pydantic import BaseModel
from clientes import Cliente


#crear el modelo transacciones (id, fecha, vr_total, cliente)
class Factura(BaseModel):
    fecha : str
    vr_total: float #calcular (cantidad * vr_unitario)
    cliente: Cliente #Relación con el cliente {objeto}


class FacturaCrear(FacturaBase):
    pass

class FacturaEditar(FacturaBase):
    pass


class Factura(FacturaBase):
    id: int | None = None