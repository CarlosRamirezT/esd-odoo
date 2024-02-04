
from odoo import api, models, fields


class HealthAppointment(models.Model):
    _name = "health.appointment"
    _description = "Manage your patient's appointments"

    name = fields.Char("Name", readonly=True)
    patient_id = fields.Many2one("health.patient", string="Patient's Name", required=True)
    doctor_id = fields.Many2one("health.doctor", string="Doctor's name", required=True)
    date = fields.Date("Appointment Date", description="The date of this appointment.", required=True)
    time = fields.Datetime("Appointment Time", description="The hour of this appointment.", required=True)
    remarks = fields.Text("Remarks", description="Any other details as per necessary")

    @api.onchange("patient_id", "doctor_id", "date")
    def _onchange_name(self):
        new_name = f"{self.patient_id.name}'s Appointment with {self.doctor_id.name} on {self.date}"
        self.name = new_name
