from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()

class Sensor(Base):
    __tablename__ = 'sensors'
    
    id = Column(Integer, primary_key=True)
    estado = Column(String)
    num_referencia = Column(Integer)
    uuid = Column(String)
    nombre = Column(String)
    conexion = Column(String)
    bateria = Column(Integer)
    
    def __init__(self, id, estado, num_referencia, uuid, nombre, conexion=False, bateria=None):
        self.id = id
        self.estado = estado
        self.num_referencia = num_referencia
        self.uuid = uuid
        self.nombre = nombre
        self.conexion = conexion
        self.bateria = bateria

class Medicion(Base):
    __tablename__ = 'mediciones'
    
    id = Column(Integer, primary_key=True)
    id_sensor = Column(Integer)
    tipo_gas = Column(String)
    latitud = Column(Float)
    longitud = Column(Float)
    fecha = Column(String)
    valor = Column(Float)
    
    def __init__(self, id, id_sensor, tipo_gas, latitud, longitud, fecha, valor):
        self.id = id
        self.id_sensor = id_sensor
        self.tipo_gas = tipo_gas
        self.latitud = latitud
        self.longitud = longitud
        self.fecha = fecha
        self.valor = valor
