from rest_framework import serializers
from webapp.models import PhelkayWord, ZhebsaWord


class PhelkayWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhelkayWord
        fields = '__all__'

class ZhebsaWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZhebsaWord
        fields = ['id','zhebsa_word','z_phrase','audio','publish_date']

class AllWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZhebsaWord
        fields = '__all__'
        depth = 1

class ZhebsaPhelkaySerializer(serializers.ModelSerializer):
    class Meta:
        model = ZhebsaWord
        fields = ['id','phelkay']
