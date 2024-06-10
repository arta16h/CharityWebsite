# In the name of GOD

from celery.app import shared_task

@shared_task()
def send_sms_otp(otp_code, mobile_number):
    pass


@shared_task()
def send_email_otp(otp_code, email):
    pass

