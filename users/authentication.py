# In the name of GOD

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.conf import settings
from django.http.request import HttpRequest

from rest_framework.exceptions import AuthenticationFailed, ParseError

from .models import User

from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from datetime import datetime


class OtpAuthBackend(ModelBackend):

    def authenticate(self, request: HttpRequest, otp_code=None, **kwargs):
        try:
            otp_identifier = request.session.get('otp-identifier')
            user = User.objects.filter(Q(phone=otp_identifier) | Q(email=otp_identifier))
            if self.verify_otp(request, otp_code) and user.exists():
                return user.get()
            raise AuthenticationFailed(_("Register First"))
        except User.DoesNotExist:
            raise AuthenticationFailed(_("Phone Number Does Not Exist"))
        
    def verify_otp(self, request: HttpRequest, otp_code):
        otp_expire_time = request.session.get("otp_expire_time")
        if otp_expire_time:
            otp_expire_time = datetime.fromisoformat(otp_expire_time)
            if otp_expire_time > timezone.now():
                if otp_code and request.session.get("otp_code") == otp_code:
                    return True
                else:
                    raise AuthenticationFailed(_("Invalid OTP"))
            else:
                raise AuthenticationFailed(_("OTP has been expired"))
        else:
            raise AuthenticationFailed(_("OTP has been expired"))


    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return


