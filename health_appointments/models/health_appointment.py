import random
import string

from odoo import api, models, fields, exceptions


class HealthAppointment(models.Model):
    _name = "health.appointment"
    _description = "Manage your patient's appointments"

    # sql constraints

    _sql_constraints = [

        # prevent more than one appointment per doctor, per hour
        (
            "doctor_date_unique",
            "unique(doctor_id, date, time)",
            "You can only book one appointment per hour for each doctor! Select a different hour or a different doctor.",
        )

    ]

    # field declarations

    name = fields.Char(
        "Name",
        readonly=True,
    )
    display_name = fields.Char(
        "Display Name",
        readonly=True,
        compute="_compute_name",
        store=True,
    )
    patient_id = fields.Many2one(
        "res.partner",
        string="Patient's Name",
        required=True,
        domain="[('is_patient', '=', True)]",
    )
    doctor_id = fields.Many2one(
        "health.doctor", string="Doctor's name", required=True
    )
    date = fields.Date(
        "Appointment Date",
        help="The date of this appointment.",
        required=True,
    )
    time = fields.Float(
        "Appointment Time",
        help="The hour of this appointment.",
        required=True,
    )
    remarks = fields.Text(
        "Remarks", help="Any other details as per necessary"
    )

    # compute, inverse, search and onchange methods

    @api.depends("patient_id", "doctor_id", "date")
    def _compute_name(self):
        for appointment in self:
            appointment.display_name = appointment._get_appointment_name()

    # selection and get methods

    @api.model
    def _get_appointment_code(self):
        chars = string.digits
        return "".join(random.choice(chars) for _ in range(8))

    def _get_appointment_name(self):
        if self.patient_id and self.doctor_id and self.date:
            return (
                f"{self.patient_id.name}'s Appointment with "
                f"{self.doctor_id.name} "
                f"on {self.date}"
            )
        else:
            return False

    # constraint methods

    @api.constrains("doctor_id", "date", "time")
    def _check_doctor_availability(self):
        for appointment in self:
            if not self.doctor_id.is_available(
                date=appointment.date, hour=appointment.time
            ):
                raise exceptions.ValidationError(
                    "The selected doctor is not available at the appointment time. "
                    "Please select another time or doctor."
                )

    # CRUD override methods
    @api.model
    def create(self, vals):
        new_code = self._get_appointment_code()
        vals.update(name=new_code)
        return super(HealthAppointment, self).create(vals)
