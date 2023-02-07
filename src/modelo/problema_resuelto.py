from pymodm import MongoModel, fields, connect
connect('mongodb+srv://robot:123@botcodeanalyzer.4rc8gsx.mongodb.net/?retryWrites=true&w=majority')

class ProblemaResuelto(MongoModel):
    nombre_usuario = fields.CharField(primary_key=True, max_lenght=50)
    servidor_usuario = fields.CharField(max_lenght=50)
    nivel_problema = fields.ListField(max_lenght=50)
    
    def __init__(self, nombre_usuario, servidor_usuario, nivel_problema):
        self.nombre_usuario=nombre_usuario
        self.servidor_usuario=servidor_usuario
        self.nivel_problema=nivel_problema
