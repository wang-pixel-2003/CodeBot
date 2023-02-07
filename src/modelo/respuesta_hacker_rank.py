from pymodm import MongoModel, fields, connect
connect('mongodb://')

class RespuestaHackerRank(MongoModel):
    problema_ID = fields.CharField(primary_key=True, max_lenght=50)
    nombre_usuario = fields.CharField(max_lenght=50)
    servidor = fields.CharField(max_lenght=50)
    pruebas_concretas = fields.ListField(max_lenght=50)
    codigo_final = fields.CharField(max_lenght=50)
    fecha_entrega = fields.CharField(max_lenght=50)
    hora_entrega = fields.CharField(max_lenght=50)
    
    def __init__(self, problema_ID, nombre_usuario, servidor, pruebas_concretas, codigo_final, fecha_entrega, hora_entrega):
        self.problema_ID=problema_ID
        self.nombre_usuario=nombre_usuario
        self.servidor=servidor
        self.pruebas_concretas=pruebas_concretas
        self.codigo_final=codigo_final
        self.fecha_entrega=fecha_entrega
        self.hora_entrega=hora_entrega
