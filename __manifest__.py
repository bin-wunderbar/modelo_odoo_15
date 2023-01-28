# -*- coding: utf-8 -*-
{
    'name': "application Management Grupo 5",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        This module is used to manage applications
    """,

    'author': "grupo 5",
    'website': "http://www.grupocinco.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Administration',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'crm'], #dependencias del modulo

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/menu_modulo.xml',
    ],
    # indicated that's an app
    'application': True,
    'installable': True,
}
