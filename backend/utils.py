import string
import random
from backend.models import ShortenedUrl

def generateUrl(size=6, chars=string.ascii_uppercase + string.digits):
    shortenedUrl = ''.join(random.choice(chars) for i in range(size))
    
    while (len(ShortenedUrl.objects.filter(shortenedUrl = shortenedUrl)) != 0):
        shortenedUrl = ''.join(random.choice(chars) for i in range(size))
    return shortenedUrl