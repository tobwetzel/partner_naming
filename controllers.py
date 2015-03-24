# -*- coding: utf-8 -*-
import openerp
from openerp.addons.website_sale.controllers import main


class PartnerNaming(main.website_sale):
    """
    Inherit controller from eCommerce modul to overwrite variables.
    """

    #add firstname, lastname and nickname to field list
    mandatory_billing_fields = ["name", "firstname", "lastname", "nickname", "phone", "email", "street2", "city", "country_id"]
    optional_billing_fields = ["street", "state_id", "vat", "vat_subjected", "zip"]
    mandatory_shipping_fields = ["name", "firstname", "lastname", "nickname", "phone", "street", "city", "country_id"]
    optional_shipping_fields = ["state_id", "zip"]
