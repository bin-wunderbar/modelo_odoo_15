# -*- coding: utf-8 -*-

from odoo import models, fields

class Employee(models.Model):
    _inherit = 'hr.employee'
    _description = 'Modelo heredado para incluir el campo "coordinador"'
    
    # Campo para almacenar si el empleado es de roll coordinador por defecto false
    is_coordinator = fields.Boolean(string='Es Coordinador', default=False)
