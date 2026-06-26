from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Relationship

#crear el modelo transaccion (id, cantidad, vr_unitaria, id_factura)
class TransaccionBase(SQLModel):
    cantidad: int =Field(default=0)
    vr_unitario: float = Field(default=0.0)
    descipcion: str | None = Field(default=None)
     

class TransaccionCrear(TransaccionBase):
    pass


class TransaccionEditar(TransaccionBase):
    pass


class Transaccion(TransaccionBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    factura_id: int |None = Field(default=None, foreign_key="factura.id")
    #aqui va la relacion con el modelo factura(solo un campo)