from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class datitos(db.Model):
    rowid = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(200))
    apellido = db.Column(db.String(200))
    fecha = db.Column(db.String(200))
    hora = db.Column(db.String(200))
    numero = db.Column(db.String(200))
    marcaciones = db.relationship('models.marcaciones', backref='datitos')
    

    def __init__(self, nombre, apellido, fecha, hora, numero):
        super().__init__()
        self.nombre = nombre
        self.apellido = apellido
        self.fecha = fecha
        self.hora = hora
        self.numero = numero

    def __str__(self):
        return "Nombre: {}. Apellido; {}. Fecha: {}. Hora; {}. Numero: {}".format(
            self.nombre,
            self.apellido,
            self.fecha,
            self.hora,
            self.numero
        )
    
    def serialize(self):
        return{
            "nombre": self.nombre,
            "apellido": self.apellido,
            "fecha" : self.fecha,
            "hora" : self.hora,
            "numero": self.numero
        }

class marcaciones(db.Model):
    rowid = db.Column(db.Integer, primary_key = True)
    fecha = db.Column(db.String(200))
    hora = db.Column(db.String(200))
    numero = db.Column(db.String(200), db.ForeignKey('datitos.numero'))

    def __init__(self, fecha, hora, numero):
        super().__init__()
        self.fecha = fecha
        self.hora = hora
        self.numero = numero

    def __str__(self):
        return "Fecha: {}. Hora; {}. Numero: {}".format(
            self.fecha,
            self.hora,
            self.numero
        )
    def serialize(self):
        return{
        "fecha" : self.fecha,
        "hora" : self.hora,
        "numero": self.numero
    }
