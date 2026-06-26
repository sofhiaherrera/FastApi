from pydantic import BaseModel, computed_field
from sqlmodel import SQLModel, Field, Relationship
from modelos.transacciones import Transaccion
from modelos.clientes import Cliente, ClienteLeer
from datetime import datetime






#crear el modelo transacciones (id, fecha, vr_total, cliente)
class FacturaBase(SQLModel):
    fecha : str = Field(default=datetime.now())
    #cliente: Cliente #Relación con el cliente {objeto}
    #transacciones: list [Transaccion] =[]

    @computed_field
    @property
    def vr_total(self) -> float:
        #calcular(cantidad * vr_unitario)
        #consultar el id actual de factura
        #factura_id_actual = getattr(self, "id", None)
        #total_factura = 0.0
        #if not factura_id_actual or not self.transacciones:
            #return total_factura
        #recorrer la lista de transacciones, segun el factura id
        #for transaccion in self.transacciones:
            #if transaccion.factura_id == factura_id_actual:
                #total_factura += transaccion.vr_unitario * transaccion.cantidad

        return 0.0


class FacturaCrear(FacturaBase):
    pass


class FacturaEditar(FacturaBase):
    pass


class Factura(FacturaBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    cliente_id: int | None = Field(default=None, foreign_key="cliente.id")
    #crear relaciones virtuale con cliente NO en BD
    cliente : Cliente = Relationship(back_populates="factura")

#crea modelo para mostrar el usuario o el cliente
class FacturaLeer(FacturaBase):
    id: int 
    cliente: ClienteLeer