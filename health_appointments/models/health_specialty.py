from odoo import fields, models


class HealthSpecialty(models.Model):
    _name = "health.specialty"
    _description = "Doctor's Specialties"

    name = fields.char("Specialty Name")
    description = fields.text("Specialty Details")

