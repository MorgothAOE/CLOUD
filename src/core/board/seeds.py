# ARCHIVO DE PRUEBA, PARA POPULAR LA BD CON DATOS DE PRUEBA
# ESTE ARCHIVO SE IMPORTA EN __init__.py DE LA APLICACION
# Y SE DEFINE UN COMANDO PARA EJECUTARLO EN LA TERMINAL
from src.core.bcrypt import bcrypt
from src.core import orders
from src.core import providers
from src.core import materials
import datetime


def run():
    """
    Deberia cargar algunos ejemplos de ordenes emitidas a modo de tener algo en la bd que traer ante consultas
    """
    print("Rellenando la base de datos con datos de prueba...")

    """
    --------------------------------------------------------------------------
        SE CREAN LOS MATERIALES
    --------------------------------------------------------------------------
    """
    material1 = materials.create_materials(
        nombre  ="plastico"
    )
    material2 = materials.create_materials(
        nombre  ="carton"
    )
    material3 = materials.create_materials(
        nombre  ="hierro"
    )
    material4 = materials.create_materials(
        nombre  ="aluminio"
    )
    """
    --------------------------------------------------------------------------
        SE CREAN LOS PROVEDORES
    --------------------------------------------------------------------------
    """
    provider1 = providers.create_provider(
        email = "cosmefulanos@gmail.com",
        nombre_deposito = "Tolosus",
        password = "juan123"
    )
    provider2 = providers.create_provider(
        email = "cosmefulano@gmail.com",
        nombre_deposito = "Hornos",
        password = "juan123"
    )
    
    """
    --------------------------------------------------------------------------
        SE CREAN LAS ORDENES
    --------------------------------------------------------------------------
    """
    orden1 = orders.create_order(
        provider_id = provider2.id,
        material_id = material1.id,
        cantidad = "20.4",
        entregado = False
    )
    orden2 = orders.create_order(
        provider_id = provider2.id,
        material_id = material2.id,
        cantidad = "53.7",
        entregado = False
    )
    orden3 = orders.create_order(
        provider_id = provider1.id,
        material_id = material3.id,
        cantidad = "12.3",
        entregado = False
    )
    #orders.assign_material(material1,orden1)
    #orders.assign_provider(provider2,orden1)
