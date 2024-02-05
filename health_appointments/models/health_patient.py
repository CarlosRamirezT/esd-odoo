
from odoo import models, fields


class HealthPatient(models.Model):
    _inherit = "res.partner"

    is_patient = fields.Boolean("Is a patient", help="Indicate whether this contact is a patient or not.")
    clinical_history = fields.Text("Clinical History")
