# -*- coding: utf-8 -*-

from odoo import models, fields, api

class appHours(models.Model):
    _name = 'app.hours'
    _description = 'Modelo que registra las horas trabajadas en cada aplicación'

    # Campo relacional para vincular empleado con las horas
    employee_id = fields.Many2one('hr.employee', string='Empleado', required=True, help='Empleado asociado a la aplicación')

    # Campo relacional para vincular las horas con una app
    app_id = fields.Many2one('app.info', string='Aplicación', required=True)

    # Campo para almacenar la fecha de la creacion de una app
    date = fields.Date(default=lambda d: fields.Date.today())
    
    # Campo para almacenar horas trabajadas en una app
    hours = fields.Integer(string='Horas trabajadas')

    # Aplicar restricción solamenete el usuario puede modificar sus horas de una app
    @api.model
    def write(self, vals):
        for record in self:
            if record.employee_id.id != self.env.user.employee_id.id:
                raise exceptions.AccessError("No tienes permiso para editar este registro.")
        return super(appHours, self).write(vals)
    
    # Aplicar restricción en la búsqueda de registros.
    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        if self.env.user.employee_id:
            args += [('employee_id', '=', self.env.user.employee_id.id)]
        return super(appHours, self).search(args, offset=offset, limit=limit, order=order, count=count)

    # Asegurar de que el campo emplyee_id y date son unicos
    _sql_constraints = [
        ('unique_employee_date', 'unique(employee_id, date)', 'Ya existe un registro con ese empleado y fecha.'),
    ]