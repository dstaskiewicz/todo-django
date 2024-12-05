from django.contrib import admin
from todogamesapp.models import User, Game, GameSeries, UserGame

# Register your models here.

class GameAdmin(admin.ModelAdmin):
    list_display = ["name", "series_id", "genre", "release_year", "image"]
    search_fields = ["name"]
    list_filter = ["genre"]

class GameSeriesAdmin(admin.ModelAdmin):
    list_display = ["name", "total_number_of_games", "genre", "developer"]
    search_fields = ["name"]
    list_filter = ["genre"]

class UserAdmin(admin.ModelAdmin):
    list_display = ["name", "id", "email", "time_created"]
    search_fields = ["name", "email"]
    list_filter = ["time_created"]

class UserGameAdmin(admin.ModelAdmin):
    list_display = ["user_id", "game_id", "status", "started_date", "completed_date"]
    search_fields = ["user_id__exact"]
    list_filter = ["status"]

admin.site.register(User, UserAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(GameSeries, GameSeriesAdmin)
admin.site.register(UserGame, UserGameAdmin)