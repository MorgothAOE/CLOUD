from flask import flash

# IMPORTO FUNCIONES PARA VALIDAR DATOS DE LOS FILTROS
from datetime import datetime
import re

# CREO UN DICCIONARIO, CON LOS POSIBLES COLORES DE LOS ESTADOS
color = {
    "En proceso": "secondary",
    "Aceptada": "info",
    "Rechazada": "danger",
    "Cancelada": "warning",
    "Finalizada": "success"
}

# DATOS DEL FORM DE UPDATE, CUANDO LA SOLICITUD TIENE EL ESTADO "EN_PROCESO"
en_proceso = [("", "Elija una opcion..."),
              ("ACEPTADA", "Aceptada"),
              ("RECHAZADA", "Rechazada")]

# DATOS DEL FORM DE UPDATE, CUANDO LA SOLICITUD TIENE EL ESTADO "ACEPTADA"
aceptada = [("", "Elija una opcion..."),
            ("CANCELADA", "Cancelada"),
            ("FINALIZADA", "Finalizada")]

"""
    FUNCION PARA VALIDAR QUE LAS FECHAS CUMPLAN 
    CON EL FORMATO 'DD/MM/YYYY - DD/MM/YYYY'
    Y QUE LA PRIMERA FECHA, NO SUPERE A LA SEGUNDA
"""


def validate_fechas(data):
    if not re.match(r'^\d{2}/\d{2}/\d{4}\s-\s\d{2}/\d{2}/\d{4}$', data):
        flash("Formato invalido de fecha. Utilize 'DD/MM/YYYY - DD/MM/YYYY'",
              "error")
        return False
    fecha_inicio, fecha_fin = data.split(' - ')
    fecha_inicio = datetime.strptime(fecha_inicio, '%d/%m/%Y')
    fecha_fin = datetime.strptime(fecha_fin, '%d/%m/%Y')
    if fecha_inicio <= fecha_fin:
        return True
    else:
        flash("La fecha de inicio debe ser menor o igual a la fecha de fin",
              "error")
        return False


# CHEQUEO SI EL TIPO DE SERVICIO ES EL DEFAULT O ES UNA INCORRECTO
def check_type_application(type): return type == "TODOS" or (
    type != "ANALISIS" and type != "CONSULTORIA" and type != "DESARROLLO")

# CHEQUEO SI EL ESTADO DE SERVICIO ES EL DEFAULT O ES UNA INCORRECTO


def check_state_application(state): return state == "TODOS" or (
    state != "EN_PROCESO" and
    state != "ACEPTADA" and
    state != "RECHAZADA" and
    state != "CANCELADA" and
    state != "FINALIZADA")

# CHEQUEO SI EL TIPO DE BUSQUEDA ES EL DEFAULT O ES UNA INCORRECTO


def check_type_search(type): return type == "TODOS" or (
    type != "EMAIL" and type != "USER")


def validate_application(id):
    """
        FUNCION UTILIZADA EN UPDATE, PARA VALIDAR 
        QUE EL NUMERO DE SOLICITUD SEA VALIDO Y ADEMAS QUE
        SE CORRESPONDA CON UNA SOLICITUD EXISTENTE
    """

    # VERIFICO QUE EL ID PASADO NO SEA INVALIDO
    if id:

        # OBTENGO LA SOLICITUD DE SERVICIO QUE SE SOLICITO CAMBIAR
        application = services.get_application_by_id(id)

        # SI LA SOLICITUD EXISTE, LA RETORNO SATISFACTORIAMENTE
        if application:
            return True, application
        else:
            flash("La solicitud pedida no existe", "error")
            return False, None
    else:
        flash("La solicitud pedida es invalida", "error")
        return False, None


def validate_change(before, after):
    """
        FUNCION PARA VALIDAR QUE EL CAMBIO QUE SE VAYA A REALIZAR SEA
    """

    if before == "EN_PROCESO" and (after == "ACEPTADA"
                                   or after == "RECHAZADA"):
        return True
    elif before == "ACEPTADA" and (after == "FINALIZADA"
                                   or after == "CANCELADA"):
        return True
    else:
        flash("El cambio realizado es invalido", "error")
        return False
