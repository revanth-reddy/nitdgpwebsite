from rest_framework import serializers
from .models import *

class JournalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Journal
        fields = ('title', 'authors', 'journal', 'vol_or_page', 'publisher', 'category', 'doi', 'year')


class ConferenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Conference
        fields = ('citation', 'location', 'year')


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('title', 'file', 'url')


class PatentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patent
        fields = ('title', 'patent_inventor', 'patent_filed_year', 'patent_Granted_year', 'patent_status', 'link', 'file')
