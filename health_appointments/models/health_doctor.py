from odoo import fields, models


class HealthDoctor(models.Model):
    _name = "health.doctor"
    _inherit = "res.partner"
    _description = "Your hospital doctors"

    tag_ids = fields.Many2many(
        "health.specialty",
        string="Doctor Specialties",
        help="Indicate the medicine expertise of each doctor.",
    )
