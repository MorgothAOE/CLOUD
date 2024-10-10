# ARCHIVO DE PRUEBA, PARA POPULAR LA BD CON DATOS DE PRUEBA
# ESTE ARCHIVO SE IMPORTA EN __init__.py DE LA APLICACION
# Y SE DEFINE UN COMANDO PARA EJECUTARLO EN LA TERMINAL
from src.core.bcrypt import bcrypt
from src.core import orders
import datetime


def run():
    """
    Deberia cargar algunos ejemplos de ordenes emitidas a modo de tener algo en la bd que traer ante consultas
    """
    print("Rellenando la base de datos con datos de prueba...")

    """
    --------------------------------------------------------------------------
        SE CREAN LAS ORDENES
    --------------------------------------------------------------------------
    """
    orden1 = orders.create_order(
        material="carton",
        cantidad=5.6
    )
