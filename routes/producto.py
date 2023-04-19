from fastapi import APIRouter
from config.db import engine
from sqlalchemy import text
from model.model_producto import ModelProducto

producto = APIRouter()

@producto.get("/producto")
def listar_producto():

    with engine.connect() as conn:
        result = conn.execute(text("select * from producto")).fetchall()
        conn.commit()
        listProducto = []
        for row in result:
            listProducto.append({"id":row.id,"nombre":row.nombre,"precio":row.precio})
    return listProducto




@producto.get("/producto/{prd_id}")
def listar_producto(prd_id: int):
    with engine.connect() as conn:
        result = conn.execute(text("select * from producto where  id = '"+str(prd_id)+"'")).fetchall()
        conn.commit()
        listProducto = []
        for row in result:
            listProducto.append({"id":row.id,"nombre":row.nombre,"precio":row.precio})
    return listProducto





@producto.post("/producto/save")
async def crear_producto(prd: ModelProducto):
    with engine.connect() as conn:
        if int(prd.id) > 0 :
            result = conn.execute(text("update producto set nombre = '"+prd.nombre+"', precio ='"+str(prd.precio)+"' where id = '"+str(prd.id)+"'"))
        else:
            result = conn.execute(text("insert into producto(nombre, precio)VALUES('"+prd.nombre+"','"+str(prd.precio)+"')"))
	    
        conn.commit()
    return {}


@producto.delete("/producto/delete/{prd_id}")
async def delete_producto(prd_id: int):
    with engine.connect() as conn:
        result = conn.execute(text("delete from producto where id = '"+str(prd_id)+"'"))
        conn.commit()
    return {}


