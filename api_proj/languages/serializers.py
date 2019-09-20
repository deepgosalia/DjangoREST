from rest_framework import serializers
from .models import Language,Paradigm,Programmer

class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    # modelSerializer has everything that u want ot do with ur mdodel
    # u can create ur own serializer but this is the best way
    class Meta:
        model = Language
        fields = ('id','url','name','paradigm')


class ParadigmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paradigm
        fields = ('id','url','name')



class ProgrammerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Programmer
        fields = ('id','url','name','languages')
"""
    
class LanguageSerializer(serializers.ModelSerializer):
    # modelSerializer has everything that u want ot do with ur mdodel
    # u can create ur own serializer but this is the best way
    class Meta:
        model = Language
        fields = ('id','name','paradigm')
"""

