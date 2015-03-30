# -*- coding: utf-8 -*-
from openerp import models, fields


class NamePartner(models.Model):
    """
    Class that inherits res.partner
    """
    _inherit = "res.partner"

    # add fields to res.partner
    firstname = fields.Char(string='First Name')
    lastname = fields.Char(string='Last Name')
    nickname = fields.Char(string='Nick Name')