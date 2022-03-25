from django.contrib import admin
from .models import Testimonial, Address, Phone, Email, Team, Social, Mission, Vision, HomeVideo, ClientEmail, RepliedEmail, EmailCount


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name", "company", "text", "rating")


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name", "field1", "field2", "field3")


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name", "number")


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name", "email")


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name", "title", "image")


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    search_fields = ("id",)
    list_display = ("facebook", "twitter", "linkedIn", "instagram", "whatsapp")


@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name", "text")


@admin.register(Vision)
class VisionAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name", "text")


@admin.register(HomeVideo)
class HomeVideoAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_display = ("title", "link")


@admin.register(ClientEmail)
class ClientEmailAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("id", "name", "message", "subject",
                    "email", "phone", "answered")


@admin.register(RepliedEmail)
class RepliedEmailAdmin(admin.ModelAdmin):
    search_fields = ("email",)
    list_display = ("email", "message", "pkey")


@admin.register(EmailCount)
class EmailCountAdmin(admin.ModelAdmin):
    search_fields = ("email",)
    list_display = ("id", "totalMail", "repliedMail", "unrepliedMail")
