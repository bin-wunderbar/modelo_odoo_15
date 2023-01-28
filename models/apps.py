# -*- coding: utf-8 -*-

from odoo import models, fields

class appInfo(models.Model):
    _name = 'app.info'
    _description = 'Application Information'

    # Campo para almacenar el nombre de la aplicación
    name = fields.Char(string='Nombre', required=True, help='Este es el nombre')

    # Campo para almacenar la descripción de la aplicación
    description = fields.Text(string='Descripcion', help='Descripción de la aplicación' )

    # Campo para almacenar la fecha de finalización de la aplicación
    finish_date = fields.Date(string='Fecha finalizacion', help='Fecha de finalización de la aplicación')

    # Campo relacional para vincular la aplicación con un cliente específico
    partner_id = fields.Many2one('res.partner', string='Cliente', help='Cliente asociado a la aplicación')

    # Campo relacional para vincular la aplicación con un responsable
    responsible_communication_id = fields.Many2one('hr.employee', string='Responsible Communication', domain=[('is_coordinator', '=', True)], help='Responsable de la aplicación')

    # Campo para almacenar si la applicacion tiene version ios
    ios_version = fields.Boolean(string='Compatible con IOS')

    # Funcion marcar todas las apps como compatible con IOS
    def mark_ios_version_tree(self):
        for record in self:
            record.ios_version = True

    # Funcion desmarcar todas las apps como compatible con IOS
    def unmark_ios_version_tree(self):
        for record in self:
            record.ios_version = False


    

