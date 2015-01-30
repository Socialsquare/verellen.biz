from partner.models import Partner
from django.utils import timezone

def user_is_expired(user):
    partner = get_partner(user)
    if partner and partner.expiryDate:
        if partner.expiryDate < timezone.now():
            return True
    return False

def get_partner(user):
    p = Partner.objects.filter(user__id=user.id)

    if p.exists():
        return p.first()

    return None
