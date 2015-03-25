# -*- coding: utf-8 -*-
import openerp
from openerp.addons.website_sale.controllers import main
import logging


class PartnerNaming(main.website_sale):
    """
    Inherit controller from eCommerce modul to overwrite variables.
    """

    #add firstname, lastname and nickname to field list
    mandatory_billing_fields = ["name", "firstname", "lastname", "phone", "email", "street2", "city", "country_id"]
    optional_billing_fields = ["street", "state_id", "vat", "vat_subjected", "zip"]
    mandatory_shipping_fields = ["name", "firstname", "lastname","phone", "street", "city", "country_id"]
    optional_shipping_fields = ["state_id", "zip"]

    def checkout_form_validate(self, data):

        _logger = logging.getLogger(__name__)

        firstname = data.get("firstname")
        lastname = data.get("lastname")

        if firstname and lastname:
            data["name"] = firstname + " " + lastname
            _logger.debug("new name: " + data.get("name"))

        if data.get("shipping_id") == -1:
            shipping_firstname = data.get("shipping_firstname")
            shipping_lastname = data.get("shipping_lastname")

            if shipping_firstname and shipping_lastname:
                data["shipping_name"] = shipping_firstname + " " + shipping_lastname

        return super(PartnerNaming, self).checkout_form_validate(data)