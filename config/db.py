from  sqlalchemy import create_engine, MetaData, URL

url_object = URL.create(
	"mysql+pymysql",
	username="appBodega",
    password="Admin123456_1",
    host="64.226.86.61",
    database="DB_BODEGA"
)

engine = create_engine(url_object)

