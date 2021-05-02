from app.models import *
from django.db.models.signals import post_save,pre_delete
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

@receiver(post_save, sender=Trigger)
def startFocus(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "DistracNot", {"type"    : "send.options","name":instance.name,"lang":instance.lang})

# @receiver(pre_delete, sender=Trigger)
# def stopFocus(sender, instance, **kwargs):
#     channel_layer = get_channel_layer()
#     async_to_sync(channel_layer.group_send)(
#     "DistracNot", {"type"    : "send.options","chk":"stop"})
