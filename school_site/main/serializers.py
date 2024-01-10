

"""
from rest_framework import serializers
from .models import SiteMenu


class menuserializer(serializers.ModelSerializer):
    class Meta:
        model = SiteMenu
        fields = ['name']


class submenuserializer(serializers.ModelSerializer):
    class Meta:
        model = SiteMenu
        fields = ['name', 'order', 'link', 'page_type', 'is_show_top', 'is_show_left']
"""