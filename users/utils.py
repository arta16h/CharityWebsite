# In the name of GOD

from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.core.mail import BadHeaderError

from kavenegar import KavenegarAPI
import random

def generate_otp_code():
    otp_code = random.randint(
        int("1"+("0"*(settings.OTP_DIGIT_COUNT-1))), 
        int("9"+("9"*(settings.OTP_DIGIT_COUNT-1)))
        )
    return otp_code

def send_sms_otp(otp_code, mobile_number):
    # kavenegar== 1.1.2
    api = KavenegarAPI(settings.KAVENEGAR_API_KEY)
    params = {
        'receptor': mobile_number,
        'template': 'Verification',
        'token': otp_code,
        'type': 'sms',
    }
    api.verify_lookup(params)


def send_email_otp(otp_code, email):
    subject = _("Otp code: {otp_code}").format(otp_code=otp_code)
    email_template_name = "pages/authentication/email.txt"
    c = {
        "email": email,
        'token': otp_code,
    }
    content = render_to_string(email_template_name, c)
    try:
        send_mail(subject, content, settings.OTP_SENDER_EMAI,
                    [email], fail_silently=False)
        return True , ""
    except BadHeaderError:
        return _("Email Doesn't Exists ")
        


def send_otp_code(otp_code, otp_type, otp_identifier) -> int:
    if otp_type == "sms":
        send_sms_otp(otp_code, mobile_number=otp_identifier)
    elif otp_type == "email":
        send_email_otp(otp_code, email=otp_identifier)
    return otp_code



