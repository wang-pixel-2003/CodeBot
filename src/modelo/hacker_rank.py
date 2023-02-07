from pymodm import MongoModel, fields, connect
connect('mongodb://')

class HackerRank(MongoModel):
    id_problema = fields.IntegerField(primary_key=True, required=True)
    lenguaje_problema = fields.CharField(max_length=20)
    nombre_dificultad = fields.CharField(max_length=20)
    descripcion_problema = fields.CharField(max_length=500)
    porcentaje_exito = fields.Decimal128Field()
    codigo_problema = fields.CharField(max_length=2000)
    pruebas = fields.ListField()
    respuestas = fields.ListField()
    
    def __init__(self, id_problema, lenguaje_problema, nombre_dificultad, descripcion_problema, porcentaje_exito, codigo_problema, pruebas, respuestas):
        self.id_problema = id_problema
        self.lenguaje_problema = lenguaje_problema
        self.nombre_dificultad = nombre_dificultad
        self.descripcion_problema = descripcion_problema
        self.porcentaje_exito = porcentaje_exito
        self.codigo_problema = codigo_problema
        self.pruebas = pruebas
        self.respuestas = respuestas
        
    class Meta:
        connection_alias = 'bd_bot'