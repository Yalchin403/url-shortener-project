import string
import random
from paste_zone.models import PasteZone

def generateSlug(size=6, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    slug = ''.join(random.choice(chars) for i in range(size))

    while (len(PasteZone.objects.filter(slug = slug)) != 0):
        slug = ''.join(random.choice(chars) for i in range(size))
    return slug
