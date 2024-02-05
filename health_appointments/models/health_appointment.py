import random
import string

from odoo import api, models, fields, exceptions


class HealthAppointment(models.Model):
    _name = "health.appointment"
    _description = "Manage your patient's appointments"

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

    _sql_constraints = [
        (
            "doctor_date_unique",
            "unique(doctor_id, date, time)",
            "You can only book one appointment per hour for each doctor! Select a different hour or a different doctor.",
        )
    ]

    @api.model
    def create(self, vals):
        new_code = self._generate_appointment_code()
        vals["name"] = new_code
        return super(HealthAppointment, self).create(vals)

    @api.depends("patient_id", "doctor_id", "date")
    def _compute_name(self):
        for appointment in self:
            if (
                appointment.patient_id
                and appointment.doctor_id
                and appointment.date
            ):
                new_name = (
                    f"{appointment.patient_id.name}'s Appointment with "
                    f"{appointment.doctor_id.name} "
                    f"on {appointment.date}"
                )
            else:
                new_name = False
            appointment.display_name = new_name

    @api.constrains("doctor_id", "date", "time")
    def _check_doctor_availability(self):
        for appointment in self:
            doctor_schedule = self.env[
                "health.doctor.schedule"
            ].search(
                [
                    ("doctor_id", "=", appointment.doctor_id.id),
                    (
                        "day_of_week",
                        "=",
                        str(appointment.date.weekday()),
                    ),
                    ("shift_start", "<=", appointment.time),
                    ("shift_end", ">", appointment.time),
                ]
            )
            if not doctor_schedule:
                raise exceptions.ValidationError(
                    "The selected doctor is not available at the appointment time. "
                    "Please select another time or doctor."
                )

    @api.model
    def _generate_appointment_code(self):
        chars = string.digits
        return "".join(random.choice(chars) for _ in range(8))
