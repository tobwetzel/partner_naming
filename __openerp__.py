# -*- coding: utf-8 -*-
{
    'name': "Partner Naming",

    'summary': """
        Add firstname, lastname and nickname field to partners.""",

    'description': """
        The modul replaces the name field of partners in views by firstname, lastname and nickname.
        Those fields are also added to the model. They are also added to the shop checkout form.
    """,

    'author': "Tobias Wetzel",
    'website': "http://www.yourcompany.com",

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
        'res_partner_added_name_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}