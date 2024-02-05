{
    "name": "health_appointments",
    "summary": """
        Doctor/Patient Appointment Reservation.
    """,
    "description": """
        Allow users to define doctors, schedule, specialties and schedule appointments for customers.
    """,
    "author": "Carlos Ramirez",
    "website": "https://github.com/CarlosRamirezT/esd-odoo",
    "category": "Uncategorized",
    "version": "15.0.0.1",
    "depends": ["base", "mail"],
    "data": [
        "security/health_security.xml",
        "security/ir.model.access.csv",
        "views/health_specialty.xml",
        "views/health_doctors.xml",
        "views/health_patients.xml",
        "views/health_appointment.xml",
    ],
    "demo": [
        "demo/demo_health_specialty.xml",
        "demo/demo_health_doctor.xml",
        "demo/demo_health_patient.xml",
        "demo/demo_health_appointment.xml",
    ],
    "application": True,
}
