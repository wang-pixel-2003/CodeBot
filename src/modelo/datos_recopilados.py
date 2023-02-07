from pymodm import MongoModel, fields, connect
connect('mongodb://', alias= 'bd_bot')

class PreguntasUsuario(MongoModel):
    nombre_usuario = fields.CharField(primary_key=True, max_length=100)
    servidor_usuario = fields.CharField(max_length=100)
    pregunta_realizada = fields.CharField(max_length=30)
    
    def __init__(self, nombre_usuario, servidor_usuario, pregunta_realizada):
        self.nombre_usuario = nombre_usuario
        self.servidor_usuario = servidor_usuario
        self.pregunta_realizada = pregunta_realizada
        
    class Meta:
        connection_alias = 'bd_bot'