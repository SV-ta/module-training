# -*- coding: utf-8 -*-
{
    'name': "my_module",

    'summary': """
        This module is created and developed by Takumi Aizawa. 
        All credits goes to Takumi Aizawa""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Takumi Aizawa",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'IT',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
