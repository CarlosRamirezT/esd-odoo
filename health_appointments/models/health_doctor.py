from odoo import fields, models


class HealthDoctor(models.Model):
    _name = "health.doctor"
    _inherits = {"res.partner": "partner_id"}
    _description = "Your hospital doctors"

    is_doctor = fields.Boolean("Is a doctor", readonly=True)
    specialty_ids = fields.Many2many(
        comodel_name="health.specialty",
        relation="health_doctor_specialty_rel",
        column1="doctor_id",
        column2="specialty_id",
        string="Doctor Specialties",
        help="Indicate the medicine expertise of each doctor.",
    )
    schedule_day_ids = fields.One2many(
        "health.doctor.schedule", "doctor_id", string="Doctor Schedule Days"
    )
