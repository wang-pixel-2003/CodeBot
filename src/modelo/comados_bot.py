from pymodm import MongoModel, fields, connect
connect('mongodb://')

class ComandosBot(MongoModel):
    nombre_comando = fields.CharField(primary_key=True, max_lenght=50)
    descripcion = fields.CharField(max_lenght=50)
    veces_llamadas = fields.CharField(max_lenght=50)
    
    def __init__(self, nombre_comando, descripcion, veces_llamadas):
        self.nombre_comando=nombre_comando
        self.descripcion=descripcion
        self.veces_llamadas=veces_llamadas
