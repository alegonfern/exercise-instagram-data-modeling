import os
import sys
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nombre_usuario = Column(String)
    correo_electronico = Column(String)
    nombre_completo = Column(String)
    biografia = Column(String)
    foto_perfil = Column(String)

    publicaciones = relationship('Publicacion', back_populates='usuario')
    comentarios = relationship('Comentario', back_populates='usuario')
    me_gustas = relationship('MeGusta', back_populates='usuario')

class Publicacion(Base):
    __tablename__ = 'publicaciones'

    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    imagen = Column(String)
    descripcion = Column(String)
    fecha_publicacion = Column(DateTime)

    usuario = relationship('Usuario', back_populates='publicaciones')
    comentarios = relationship('Comentario', back_populates='publicacion')
    me_gustas = relationship('MeGusta', back_populates='publicacion')

class Comentario(Base):
    __tablename__ = 'comentarios'

    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    publicacion_id = Column(Integer, ForeignKey('publicaciones.id'))
    texto_comentario = Column(String)

    usuario = relationship('Usuario', back_populates='comentarios')
    publicacion = relationship('Publicacion', back_populates='comentarios')

class MeGusta(Base):
    __tablename__ = 'me_gustas'

    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    publicacion_id = Column(Integer, ForeignKey('publicaciones.id'))

    usuario = relationship('Usuario', back_populates='me_gustas')
    publicacion = relationship('Publicacion', back_populates='me_gustas')

def to_dict(self):
    return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e