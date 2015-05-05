# -*- coding: utf-8 -*-
{
    'name': "Partner Naming",

    'summary': """
        Add firstname, lastname and nickname field to partners.""",

    'description': """
        The module adds fields for first and last name to the res.partner model and related views.
        They are also added to the shop checkout form.
    """,

    'author': "Tobias Wetzel",
    'website': "https://github.com/tobwetzel/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'website_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
        'views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}