from flask import request


from flask import flash



def paginate(Query, **kwargs):
    # Obtengo la pagina actual
    page = request.args.get('page', 1, type=int)

    # Obtengo la cantidad elementos por pagina
    rows = configuration.get_configuration().n_elements_by_page

    if kwargs:
        id = kwargs.get("id", None)
        return Query(id_inst=id, page=page, rows=rows)
    else:
        return Query(page=page, rows=rows)
    


def paginate_application(Query, id, form):
    # Obtengo la pagina actual
    page = request.args.get('page', 1, type=int)

    # Obtengo la cantidad elementos por pagina
    rows = configuration.get_configuration().n_elements_by_page

    type_service = form.type_service.data
    fechas = form.fechas.data
    state_application = form.state_application.data
    search_type = form.search_type.data
    search = form.search.data
    order = form.order.data

    # OBTENGO LAS SOLICITUDES DE LA INSTITUCION, SIN FILTROS
    return Query(id, 
                 type_service, 
                 fechas, 
                 state_application, 
                 search_type, 
                 search, order, 
                 page=page, 
                 rows=rows)

    
    
def paginate_search_user(Query, **kwargs):
    # Obtengo la pagina actual
    page = request.args.get('page', 1, type=int)

    # Obtengo la cantidad elementos por pagina
    rows = configuration.get_configuration().n_elements_by_page

    texto_busqueda = request.form.get('texto_busqueda')
    b = request.form.get('busqueda')
    c = request.form.get('activos')
    act = -1
    if (c != 'todos'):
        if (c == 'activo'):
            act = 1
        else:
            act = 0
    return Query(
        page=page, rows=rows,
        s=texto_busqueda,
        parameter=b,
        active=act
    )