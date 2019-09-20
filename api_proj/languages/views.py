from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Language, Paradigm, Programmer
from .serializers import LanguageSerializer, ParadigmSerializer, ProgrammerSerializer


class LanguageView(viewsets.ModelViewSet):
    # this modeview will handle all request
    # like put push get...so we use it instead of defiing ourselves
    queryset = Language.objects.all()  # this will give all data
    serializer_class = LanguageSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)  to prevent writing in individual classes we have written it in setting part


class ParadigmView(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()  # this will give all data
    serializer_class = ParadigmSerializer


class ProgrammerView(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()  # this will give all data
    serializer_class = ProgrammerSerializer
