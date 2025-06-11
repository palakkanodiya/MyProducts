#handle kregA emails isle ye create ki file

from django.core.mail import send_mail
import random

#jisse email send krna usse layege abh
from django.conf import settings

#otp send k bd particularly uss user ko otp send bi krna hoga uske lie USER MODEL ko bulayege
from .models import User


def send_otp_vie_email(email):
    subject = 'your account verification email'
    otp = random.randint(1000,9999)
    message = f'your otp {otp}'
    email_from = settings.EMAIL_HOST
    send_mail(subject, message , email_from , [email])  #email[] isme list m aayega
    #user_obj m us user ko put krdege
    user_obj = User.objects.get(email = email)

    #yha pr otp ko save krpayege
    user_obj.otp = otp
    user_obj.save()