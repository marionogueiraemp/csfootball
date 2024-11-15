from django.db.models.signals import post_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .models import Notification
from teams.models import PlayerApplication, TransferRequest
from competitions.models import Match


@receiver(post_save, sender=PlayerApplication)
def notify_team_application(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.team.owner,
            message=f"New application from {
                instance.player.username} to join {instance.team.name}."
        )


@receiver(post_save, sender=TransferRequest)
def notify_transfer_request(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.to_team.owner,
            message=f"Transfer request for {instance.player.username} from {
                instance.from_team.name} to {instance.to_team.name}."
        )


@receiver(post_save, sender=Match)
def notify_match_result(sender, instance, **kwargs):
    if instance.team1_score is not None and instance.team2_score is not None:
        Notification.objects.create(
            user=instance.competition.league_manager,  # Example recipient
            message=f"Match result: {instance.team1.name} {
                instance.team1_score} - {instance.team2_score} {instance.team2.name}"
        )


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
