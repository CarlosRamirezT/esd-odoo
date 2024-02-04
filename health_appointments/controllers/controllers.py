# -*- coding: utf-8 -*-
# from odoo import http


# class HealthAppointments(http.Controller):
#     @http.route('/health_appointments/health_appointments', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/health_appointments/health_appointments/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('health_appointments.listing', {
#             'root': '/health_appointments/health_appointments',
#             'objects': http.request.env['health_appointments.health_appointments'].search([]),
#         })

#     @http.route('/health_appointments/health_appointments/objects/<model("health_appointments.health_appointments"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('health_appointments.object', {
#             'object': obj
#         })
