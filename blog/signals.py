from django.dispatch import receiver
from django.db.models import signals
from .models import Post
from django.core.mail import send_mail

import logging


logger = logging.getLogger(__name__)

@receiver(signals.post_save, sender=Post)
def send_post_mail(sender, instance, created, **kwargs):
    print('signal send')
    logger.error("signal recieve")
    subject = "Thank you for registering with us"
    send_mail(subject, 'Body', 'khdhoney@gmail.com',['hitesh.khandelwal_ug21@ashoka.edu.in'], fail_silently=False,)
        
    