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
        "views/health_specialty_views.xml",
        "views/health_doctors_views.xml",
        "views/health_patients_views.xml",
        "views/health_appointment_views.xml",
        "views/module_menus.xml",
    ],
    "demo": [
        "data/health_specialty_demo.xml",
        "data/health_doctor_demo.xml",
        "data/health_patient_demo.xml",
        "data/health_appointment_demo.xml",
    ],
    "application": True,
}
