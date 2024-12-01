from django.contrib import admin
from .models import Competition, Match, PlayerStats


@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    list_display = ('name', 'competition_type',
                    'start_date', 'end_date', 'is_active')
    list_filter = ('competition_type', 'is_active')
    search_fields = ('name',)


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('competition', 'home_team',
                    'away_team', 'match_date', 'status')
    list_filter = ('competition', 'status')
    search_fields = ('home_team__name', 'away_team__name')


@admin.register(PlayerStats)
class PlayerStatsAdmin(admin.ModelAdmin):
    list_display = ('player', 'match', 'goals', 'assists',
                    'yellow_cards', 'red_cards')
    list_filter = ('match',)
    search_fields = ('player__username',)
