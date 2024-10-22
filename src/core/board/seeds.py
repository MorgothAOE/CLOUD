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
    fecha7 = datetime.datetime.now()
    fecha7 = fecha7 + datetime.timedelta(days=7)
    fecha14 = datetime.datetime.now()
    fecha14 = fecha7 + datetime.timedelta(days=14)
    fecha31 = datetime.datetime.now()
    fecha31 = fecha31 + datetime.timedelta(days=31)
    fecha280 = datetime.datetime.now()
    fecha280 = fecha280 + datetime.timedelta(days=280)

    """
    --------------------------------------------------------------------------
        SE CREAN LOS MATERIALES
    --------------------------------------------------------------------------
    """
    mplastico = materials.create_materials(
        nombre  ="plastico"
    )
    mcarton = materials.create_materials(
        nombre  ="carton"
    )
    mhierro = materials.create_materials(
        nombre  ="hierro"
    )
    maluminio = materials.create_materials(
        nombre  ="aluminio"
    )
    """
    --------------------------------------------------------------------------
        SE CREAN LOS PROVEDORES
    --------------------------------------------------------------------------
    """
    provider1 = providers.create_provider(
        email = "tolosa@gmail.com",
        nombre_deposito = "Tolosa",
        password = "juan123"
    )
    provider2 = providers.create_provider(
        email = "lhornos@gmail.com",
        nombre_deposito = "Los Hornos",
        password = "juan123"
    )
    provider3 = providers.create_provider(
        email = "saveedra@gmail.com",
        nombre_deposito = "Parque Saavedra",
        password = "juan123"
    )
    
    """
    --------------------------------------------------------------------------
        SE ASIGNAN LOS MATERIALES
    --------------------------------------------------------------------------
    """
    providers.add_for_material(
        provider_id=provider1.id,
        material_id=mplastico.id
    )
    providers.add_for_material(
        provider_id=provider1.id,
        material_id=maluminio.id
    )
    providers.add_for_material(
        provider_id=provider2.id,
        material_id=mhierro.id
    )
    providers.add_for_material(
        provider_id=provider2.id,
        material_id=mcarton.id
    )
    """
    --------------------------------------------------------------------------
        SE CREAN LAS ORDENES
    --------------------------------------------------------------------------
    """
    orden1 = orders.create_order(
        available_until=fecha14,
        provider_id = provider2.id,
        material_id = mhierro.id,
        cantidad = "20.4",
        delivered = False,
        reserved = True,
        reserved_at = datetime.datetime.now()
    )
    orden2 = orders.create_order(
        available_until=fecha31,
        provider_id = provider2.id,
        material_id = mcarton.id,
        cantidad = "53.7",
        delivered = False,
        reserved = True,
        reserved_at = datetime.datetime.now()
    )
    orden3 = orders.create_order(
        available_until=fecha14,
        provider_id = provider1.id,
        material_id = maluminio.id,
        cantidad = "12.3",
        delivered = False,
        reserved = True,
        reserved_at = datetime.datetime.now()
    )
    orden4 = orders.create_order(
        available_until=fecha280,
        material_id = maluminio.id,
        cantidad = "7142.3"
    )
    orden5 = orders.create_order(
        available_until=fecha31,
        material_id = maluminio.id,
        cantidad = "80.6"
    )
    orden6 = orders.create_order(
        available_until=fecha280,
        material_id = mhierro.id,
        cantidad = "60"
    )
    orden7 = orders.create_order(
        available_until=fecha14,
        material_id = mcarton.id,
        cantidad = "35"
    )
    orden8 = orders.create_order(
        available_until=fecha31,
        material_id = mplastico.id,
        cantidad = "52"
    )
    orden9 = orders.create_order(
        available_until=fecha14,
        material_id = mhierro.id,
        cantidad = "70"
    )
    orden10 = orders.create_order(
        available_until=fecha14,
        provider_id = provider1.id,
        material_id = mplastico.id,
        cantidad = "20.4",
        delivered = True,
        reserved = True,
        reserved_at = datetime.datetime.now(),
        delivered_at = datetime.datetime.now()
    )
    #orders.assign_material(material1,orden1)
    #orders.assign_provider(provider2,orden1)
