from  sqlalchemy import create_engine, MetaData, URL

url_object = URL.create(
	"mssql+pymssql",
	username="jeremykun_SQLLogin_1",
    password="dwgu65wy9z",
    host="DBAPIAUTO.mssql.somee.com",
    database="DBAPIAUTO"
)

engine = create_engine(url_object)

