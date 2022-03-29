from rest_framework import authentication
from rest_framework import exceptions
from app.models import OauthAdmin, Admin, OauthTeacher, Teacher
from django.core.exceptions import ObjectDoesNotExist
import jwt
from raporsi.settings import SECRET_KEY


class AdminAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth = request.META.get('HTTP_AUTHORIZATION', '')
        auth = auth.split()
        if len(auth) == 0:
            msg = 'Credential required'
            raise exceptions.AuthenticationFailed(msg)
        if len(auth) == 1:
            msg = 'Invalid token header. No credentials provided.'
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = 'Invalid token header. Token string should not contain spaces.'
            raise exceptions.AuthenticationFailed(msg)
        bearer = auth[1]
        try:
            token = OauthAdmin.objects.get(token=bearer)
            if not token.is_active:
                msg = 'Invalid token header. Token is already not active or deleted.'
                raise exceptions.AuthenticationFailed(msg)
            data = jwt.decode(bearer, SECRET_KEY, algorithms=["HS256"])
            if data['id'] != token.admin_id:
                msg = 'Invalid token header. Token owner is not match.'
                raise exceptions.AuthenticationFailed(msg)
            try:
                c = Admin.objects.get(id=data['id'])
            except ObjectDoesNotExist:
                msg = 'Invalid token header. Client not found.'
                raise exceptions.AuthenticationFailed(msg)
            return None, data
        except ObjectDoesNotExist:
            msg = 'Invalid token header. Token not identified by server.'
            raise exceptions.AuthenticationFailed(msg)


class TeacherAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth = request.META.get('HTTP_AUTHORIZATION', '')
        auth = auth.split()
        if len(auth) == 0:
            msg = 'Credential required'
            raise exceptions.AuthenticationFailed(msg)
        if len(auth) == 1:
            msg = 'Invalid token header. No credentials provided.'
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = 'Invalid token header. Token string should not contain spaces.'
            raise exceptions.AuthenticationFailed(msg)
        bearer = auth[1]
        try:
            token = OauthTeacher.objects.get(token=bearer)
            if not token.is_active:
                msg = 'Invalid token header. Token is already not active or deleted.'
                raise exceptions.AuthenticationFailed(msg)
            data = jwt.decode(bearer, SECRET_KEY, algorithms=["HS256"])
            if data['id'] != token.admin_id:
                msg = 'Invalid token header. Token owner is not match.'
                raise exceptions.AuthenticationFailed(msg)
            try:
                c = Teacher.objects.get(id=data['id'])
            except ObjectDoesNotExist:
                msg = 'Invalid token header. Client not found.'
                raise exceptions.AuthenticationFailed(msg)
            return None, data
        except ObjectDoesNotExist:
            msg = 'Invalid token header. Token not identified by server.'
            raise exceptions.AuthenticationFailed(msg)
