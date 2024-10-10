
class PaginatedClass():
    def __init__(self, data, page, per_page, total, pages):
        self.data = data
        self.page = page
        self.per_page = per_page
        self.total = total
        self.pages = pages


class PromedioClass():
    def __init__(self, data, quantity):
        self.data = data
        self.quantity = quantity


class RequestedServices():
    def __init__(self, data, n_elements):
        self.data = data
        self.n_elements = n_elements

class ConfigurationClass():
    def __init__(self, contact_info):
        self.contact_info = contact_info

class ApplicationStateClass():
    def __init__(self, data):
        self.data = data

def page_per_page_parser(page, per_page):
    if (page.isdigit() and per_page.isdigit()):
        return True
    else:
        return False
