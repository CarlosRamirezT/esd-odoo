from odoo import fields, models


class HealthDoctor(models.Model):
    _name = "health.doctor"
    _description = "Your hospital doctors"

    name = fields.Char("Name", required=True)
    last_name = fields.Char("Last Name", required=True)
    identification = fields.Char("Identification", required=True)
    specialty_ids = fields.Many2many(
        comodel_name="health.specialty",
        relation="health_doctor_specialty_rel",
        column1="doctor_id",
        column2="specialty_id",
        string="Doctor Specialties",
        help="Indicate the medicine expertise of each doctor.",
    )
    schedule_day_ids = fields.One2many(
        "health.doctor.schedule",
        "doctor_id",
        string="Doctor Schedule Days",
    )

    def is_available(self, date, hour):
        """
        Checks whether a doctor in available
        a certain date at a certain hour.

        Args:
            date (date object): date to be checked
            hour (float date): hour to be checked

        Returns: health.doctor.schedule object if available, otherwise empty list.
        """
        return self.env["health.doctor.schedule"].search(
            [
                ("doctor_id", "=", self.id),
                (
                    "day_of_week",
                    "=",
                    str(date.weekday()),
                ),
                ("shift_start", "<=", hour),
                ("shift_end", ">", hour),
            ]
        )
