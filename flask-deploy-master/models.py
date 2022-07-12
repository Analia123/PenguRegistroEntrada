from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime
import pytz # Python timezone


def create_app():
    app = Flask(__name__)
    #COFIGURAMOS EL ACCESO A LA BASE DE DATOS
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///databases/bootcamp10.db" #Direccion abs en linux
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    return app

app = create_app()

db = SQLAlchemy(app)

class datitos(db.Model):
    rowid = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(200))
    apellido = db.Column(db.String(200))
    fecha = db.Column(db.String(200))
    hora = db.Column(db.String(200))
    numero = db.Column(db.String(200))
    mesa = db.Column(db.Integer)
    marcaciones = db.relationship('models.marcaciones', backref='datitos')
    

    def __init__(self, nombre, apellido, numero, mesa):
        super().__init__()
        
        deitaim = datetime.datetime.now(pytz.timezone('America/Asuncion'))

        self.nombre = nombre
        self.apellido = apellido
        self.fecha = deitaim.strftime("%d-%m-%Y")
        self.hora = deitaim.strftime("%H:%M:%S")
        self.numero = numero
        self.mesa = mesa

    def __str__(self):
        return "Nombre: {}. Apellido; {}. Fecha: {}. Hora; {}. Numero: {}".format(
            self.nombre,
            self.apellido,
            self.fecha,
            self.hora,
            self.numero,
            self.mesa
        )
    
    def serialize(self):
        return{
            "nombre": self.nombre,
            "apellido": self.apellido,
            "fecha" : self.fecha,
            "hora" : self.hora,
            "numero": self.numero,
            "mesa": self.mesa
        }

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update(self, data):
        for key, value in data.items():
            setattr(self, key, value)
        self.save()
        return self

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
