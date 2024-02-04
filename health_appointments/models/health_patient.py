
from odoo import models, fields


class HealthPatient(models.Model):
    _name = "health.patient"
    _inherits = {"res.partner": "partner_id"}

    clinical_history = fields.Text("Clinical History")
