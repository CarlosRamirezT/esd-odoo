
from odoo import models, fields


class HealthPatient(models.Model):
    _inherit = "res.partner"

    clinical_history = fields.Text("Clinical History")
