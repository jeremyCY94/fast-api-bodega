from pydantic import BaseModel


class ModelProducto(BaseModel):
    id:int
    nombre:str
    precio:float