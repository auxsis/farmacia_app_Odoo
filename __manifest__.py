{
    'name': 'Farmacia y Parafarmacia APP',
    'description': 'Control de almacen, gestion de pedidos y productos farmaceuticos y de parafarmacia',
    'author': 'Sergio Duran, Sara Andres, Sergio Martinez',
    'depends': ['base'],
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'views/farmacia_menu.xml',
        'views/producto_view.xml',
        'views/stock_view.xml',

    ],

}
