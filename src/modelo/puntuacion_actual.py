from pymodm import MongoModel, fields, connect
connect('mongodb://')

class PuntuacionActual(MongoModel):
    nombre_usuario = fields.CharField(primary_key=True, max_lenght=50)
    servidor_usuario = fields.CharField(max_lenght=50)
    puntos_obtenidos = fields.ListField(max_lenght=50)
    
    def __init__(self, nombre_usuario, servidor_usuario, puntos_obtenidos):
        self.nombre_usuario=nombre_usuario
        self.servidor_usuario=servidor_usuario
        self.puntos_obtenidos=puntos_obtenidos