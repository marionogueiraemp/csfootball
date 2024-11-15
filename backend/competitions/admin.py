from django.contrib import admin
from .models import Competition, Match, PlayerStats
import datetime

admin.site.register(Match)
admin.site.register(PlayerStats)

@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    list_display = ('name', 'competition_type', 'created_at')
    actions = ['generate_fixtures']

    def generate_fixtures(self, request, queryset):
        """
        Custom admin action to generate fixtures for selected competitions.
        """
        for competition in queryset:
            if competition.teams.count() > 1:  # Ensure there are at least 2 teams
                competition.generate_fixtures(start_date=datetime.date.today(), home_and_away=True)
                self.message_user(request, f"Fixtures generated for {competition.name}")
            else:
                self.message_user(request, f"Not enough teams to generate fixtures for {competition.name}", level='warning')

    generate_fixtures.short_description = "Generate fixtures for selected competitions"