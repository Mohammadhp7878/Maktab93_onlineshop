from django.core.exceptions import ValidationError
import re
from kavenegar import *


def validate_password(value):
    if len(value) < 8 or len(value) > 20:
        raise ValidationError("Password must be between 8 and 20 characters.")
    if not re.search(r"[A-Z]", value):
        raise ValidationError("Password must contain at least one uppercase letter.")
    if not re.search(r"\d", value):
        raise ValidationError("Password must have at least one number.")
    if not re.search(r"[!@#$%^&*()-_=+{}<>]", value):
        raise ValidationError("Password must have at least one special character.")
    

def send_otp(phone_number, code):
    try:
        api = KavenegarAPI('742F6645615078555652485A614A79754761596F314D4E32355668626F42366D6969764B6862334B456C6F3D')
        params = {
            'sender': '',#optional
            'receptor': phone_number ,#multiple mobile number, split by comma
            'message': f'your confirm code is {code}',
        } 
        response = api.sms_send(params)
        print(response)
    except APIException as e: 
        print(e)
    except HTTPException as e: 
        print(e)