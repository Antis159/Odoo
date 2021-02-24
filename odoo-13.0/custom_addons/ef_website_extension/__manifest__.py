# -*- coding: utf-8 -*-
{
    'name': "Website Extension",

    'summary': "Extend your website",

    'description': """
    - extends your website
    - very useful
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['product', 'website', 'website_sale', 'sale', 'payment'],

    # always loaded
    'data': [
        'security/groups.xml',
        'views/uom.xml',
        'views/invisible_price.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo.xml',
    # ],
    'installable': True,
    'application': False,
    'auto_install': False,
}