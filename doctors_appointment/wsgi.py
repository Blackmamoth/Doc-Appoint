"""
WSGI config for doctors_appointment project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

fake_docs = [
    {"name": "Dr. Prakash rao", "type": "Cardiologist", "email": "Dummydoc1@gmail.com", "phone": "1234567890", "address": "1st street, prakash rao clinic"},
    {"name": "Dr. Kunal Khamrai", "type": "Dentist", "email": "Dummydoc2@gmail.com","phone": "098765431" , "address": "2nd street, kunal khamrai clinic "},
    {"name": "Dr. Khushi singh", "type": "Paediatrician", "email": "Dummydoc3@gmail.com","phone": "1029384756" ,"address": "3rd street, khushi singh clinic "},
    {"name": "Dr. Kunal Sharma", "type": "Psychiatrist", "email": "Dummydoc4@gmail.com", "phone": "1083927456" ,"address": "4thnd street, kunal sharma clinic "}
]

from appointments.models import Doctor

for doc in fake_docs:
    doctor = Doctor(name=doc.get('name'), type=doc.get('type'), email=doc.get('email'), phone=doc.get('phone'), clinic_address=doc.get('address'))
    doctor.save()


from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'doctors_appointment.settings')

application = get_wsgi_application()
