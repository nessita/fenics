from django.contrib import admin

from ega.models import (
    ChampionPrediction,
    EgaUser,
    League,
    LeagueMember,
    Match,
    Prediction,
    Team,
    TeamStats,
    Tournament,
)


class EgaUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'invite_key', 'date_joined')
    search_fields = ('username', 'email', 'invite_key')
    readonly_fields = ('list_referrals',)

    def list_referrals(self, obj):
        return ', '.join(u.username for u in obj.referrals.all())


class LeagueMemberInline(admin.TabularInline):
    model = LeagueMember
    extra = 0


class LeagueAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'tournament')
    inlines = [LeagueMemberInline]


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    prepopulated_fields = dict(slug=('name',))


class TeamStatsAdmin(admin.ModelAdmin):
    list_display = ('team', 'tournament', 'zone', 'points')
    list_filter = ('tournament', 'team')


class MatchAdmin(admin.ModelAdmin):
    list_display = ('tournament', 'home', 'home_goals', 'away_goals', 'away')
    list_filter = ('tournament', 'when', 'finished')


class PredictionAdmin(admin.ModelAdmin):
    list_display = ('match', 'user', 'score', 'last_updated')
    list_filter = ('match__tournament',)


class ChampionPredictionAdmin(admin.ModelAdmin):
    list_display = ('user', 'tournament', 'team', 'last_updated')
    list_filter = ('tournament',)


class TournamentAdmin(admin.ModelAdmin):
    filter_horizontal = ('teams',)
    list_display = ('name', 'published', 'finished')
    prepopulated_fields = dict(slug=('name',))


admin.site.register(ChampionPrediction, ChampionPredictionAdmin)
admin.site.register(EgaUser, EgaUserAdmin)
admin.site.register(League, LeagueAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(Prediction, PredictionAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(TeamStats, TeamStatsAdmin)
admin.site.register(Tournament, TournamentAdmin)
