# In the name of GOD

from celery.app import shared_task
from .utils import send_otp_code, send_email_otp, send_sms_otp

@shared_task()
def async_send_sms_otp(otp_code, mobile_number):
    send_sms_otp(otp_code=otp_code, mobile_number=mobile_number)


@shared_task()
def async_send_email_otp(otp_code, email):
    send_email_otp(otp_code=otp_code, email=email)

@shared_task()
def async_send_otp(otp_code, otp_type, otp_identifier):
    send_otp_code(
        otp_code=otp_code, 
        otp_type=otp_type, 
        otp_identifier=otp_identifier
    )
