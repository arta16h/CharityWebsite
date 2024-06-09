# In the name of GOD

from kavenegar import KavenegarAPI
from django.conf import settings

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



