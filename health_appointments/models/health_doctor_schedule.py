from odoo import fields, models


class HealthDoctorSchedule(models.Model):
    _name = "health.doctor.schedule"
    _description = "Manage your doctors schedules."

    doctor_id = fields.Many2one("Doctor")
    day_of_week = fields.Selection(
        [
            ("0", "Monday"),
            ("1", "Tuesday"),
            ("2", "Wednesday"),
            ("3", "Thursday"),
            ("4", "Friday"),
            ("5", "Saturday"),
            ("6", "Monday"),
        ],
        string="Day of Week",
    )
    shift_start = fields.Datetime(string="Starting Shift Hour", widget="time")
    shift_end = fields.Datetime(string="Ending Shift Hour", widget="time")
