from apiCandidat.models import Candidat
from apiCandidat.serializers import CandidatSerializer
from apiCandidat.models import Recruteur
from apiCandidat.serializers import RecruteurSerializer
from apiCandidat.models import Partenaire
from apiCandidat.serializers import PartenaireSerializer
from apiCandidat.models import Client
from apiCandidat.serializers import ClientSerializer
from apiCandidat.models import Offre
from apiCandidat.serializers import OffreSerializer
from apiCandidat.models import Meeting
from apiCandidat.serializers import MeetingSerializer
from rest_framework import generics

#####
class CandidatList(generics.ListCreateAPIView):
    queryset = Candidat.objects.all()
    serializer_class = CandidatSerializer


class CandidatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Candidat.objects.all()
    serializer_class = CandidatSerializer
######
class RecruteurList(generics.ListCreateAPIView):
    queryset = Recruteur.objects.all()
    serializer_class = RecruteurSerializer


class RecruteurDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recruteur.objects.all()
    serializer_class = RecruteurSerializer
######

class PartenaireList(generics.ListCreateAPIView):
    queryset = Partenaire.objects.all()
    serializer_class = PartenaireSerializer


class PartenaireDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Partenaire.objects.all()
    serializer_class = PartenaireSerializer

######

class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
######

class OffreList(generics.ListCreateAPIView):
    queryset = Offre.objects.all()
    serializer_class = OffreSerializer


class OffreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Offre.objects.all()
    serializer_class = OffreSerializer
######

class MeetingList(generics.ListCreateAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer


class MeetingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer