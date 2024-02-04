from odoo import fields, models


class HealthDoctor(models.Model):
    _name = "health.doctor"
    _inherit = "res.partner"
    _description = "Your hospital doctors"

    specialty_ids = fields.Many2many(
        "health.specialty",
        string="Doctor Specialties",
        help="Indicate the medicine expertise of each doctor.",
    )
    schedule_day_ids = fields.One2many("health.doctor.schedule", "doctor_id", string="Doctor Schedule Days")
