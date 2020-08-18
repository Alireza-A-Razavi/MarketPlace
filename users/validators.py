from django.core.exceptions import ValidationError

def validate_phone_number(value):

    sane = [
        '1','2','3','4','5','6','7','8','9','0','+',
        '۱','۲','۳','۴','۵','۶','۷','۸','۹','۰',
    ]
    for num in value:
        if num not in sane:
            raise ValidationError("شماره تلفن معقول وارد کنید")
    return value