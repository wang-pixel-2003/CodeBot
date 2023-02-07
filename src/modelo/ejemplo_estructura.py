from pymodm import MongoModel, fields, connect
connect('mongodb://')

class EjemploEstructura(MongoModel):
    nombre_estructura = fields.CharField(primary_key=True, max_lenght=50)
    lenguaje_estructura = fields.CharField(max_lenght=50)
    explicacion = fields.CharField(max_lenght=50)
    codigo_estructura = fields.CharField(max_lenght=50)
    
    def __init__(self, nombre_estructura, lenguaje_estructura, explicacion, codigo_estructura):
        self.nombre_estructura=nombre_estructura
        self.lenguaje_estructura=lenguaje_estructura
        self.explicacion=explicacion
        self.codigo_estructura=codigo_estructura
