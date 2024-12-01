from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .models import Notification
from teams.models import PlayerApplication, TransferRequest
from competitions.models import Match

# Notify team owner when a player applies to a team


@receiver(post_save, sender=PlayerApplication)
def notify_team_application(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.team.owner,
            message=f"New application from {instance.player.username}"
        )

# Notify team owner about a transfer request


@receiver(post_save, sender=TransferRequest)
def notify_transfer_request(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.to_team.owner,
            message=f"Transfer request for {instance.player.username}"
        )

# Notify league manager when a match result is recorded


@receiver(post_save, sender=Match)
def notify_match_result(sender, instance, **kwargs):
    try:
        user = instance.competition.owner  # Adjust field name as needed
        if user:
            Notification.objects.create(
                user=user,
                message=f"The result for the match {instance.match}"
            )
    except ObjectDoesNotExist:
        # Handle cases where the owner does not exist
        pass

# Broadcast notification over WebSocket channels


@receiver(post_save, sender=Notification)
def broadcast_notification(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        group_name = f"notifications_{instance.user.id}"
        async_to_sync(channel_layer.group_send)(
            group_name,
            {
                "type": "send_notification",
                "message": {
                    "id": instance.id,
                    "message": instance.message,
                    "category": instance.category,
                    "is_read": instance.is_read,
                },
            },
        )
