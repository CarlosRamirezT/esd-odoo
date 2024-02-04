from odoo import fields, models


class HealthSpecialty(models.Model):
    _name = "health.specialty"
    _description = "Doctor's Specialties"

    name = fields.Char("Specialty Name")
    help = fields.Text("Specialty Details")

