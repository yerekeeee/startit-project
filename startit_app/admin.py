from django.contrib import admin
from .models import Category, Job, Guide

admin.site.register(Category)
admin.site.register(Job)
admin.site.register(Guide)