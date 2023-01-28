# -*- coding: utf-8 -*-

from odoo import models, fields

class resPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'Modelo heredado para incluir el campo "Red Social Favorita"'

    # Campo para almacenar red social favorita con seleccion 
    social_network = fields.Selection([
        ('twitter', 'Twitter'),
        ('instagram', 'Instagram'),
        ('facebook', 'Facebook')
    ], string='Red Social Favorita', default='twitter')