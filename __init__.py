from . import models
from odoo import api, fields, tools


def add_datos_prueba(cr, registry):
    tools.convert_file(cr, 'farmacia_app', 'data/farmacia.producto.csv', None, mode='init', noupdate=True,
                       kind='init', report=None)


def add_datos_proveedores(cr, registry):
    tools.convert_file(cr, 'farmacia_app', 'data/farmacia.proveedores.csv', None, mode='init', noupdate=True,
                       kind='init', report=None)

def add_datos_clientes(cr, registry):
    tools.convert_file(cr, 'farmacia_app_Odoo', 'data/farmacia.clientes.csv', None, mode='init', noupdate=True,
                        kind='init', report=None)
