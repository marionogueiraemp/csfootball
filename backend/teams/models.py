from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()


class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    logo = models.ImageField(upload_to='team_logos/', null=True, blank=True)
    owner = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='owned_team')
    players = models.ManyToManyField(User, related_name='teams', blank=True)

    def clean(self):
        # Ensure a user can only own one team
        if Team.objects.filter(owner=self.owner).exists() and self.pk is None:
            raise ValidationError("A user can only own one team.")

    def save(self, *args, **kwargs):
        self.clean()  # Call the validation logic
        super().save(*args, **kwargs)

    # Use a string reference for Competition to avoid circular import
    competitions = models.ManyToManyField(
        'competitions.Competition', related_name='teams', blank=True)

    def __str__(self):
        return self.name


class PlayerApplication(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name='applications')
    status = models.CharField(max_length=20, choices=[(
        'PENDING', 'Pending'), ('ACCEPTED', 'Accepted'), ('DECLINED', 'Declined')])
    created_at = models.DateTimeField(auto_now_add=True)


class TransferRequest(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    from_team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name='outgoing_transfers')
    to_team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name='incoming_transfers')
    status = models.CharField(max_length=20, choices=[(
        'PENDING', 'Pending'), ('ACCEPTED', 'Accepted'), ('DECLINED', 'Declined')])
    created_at = models.DateTimeField(auto_now_add=True)
