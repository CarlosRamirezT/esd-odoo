# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class health_appointments(models.Model):
#     _name = 'health_appointments.health_appointments'
#     _description = 'health_appointments.health_appointments'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
