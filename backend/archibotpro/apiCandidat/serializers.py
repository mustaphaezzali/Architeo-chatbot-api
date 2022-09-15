from rest_framework import serializers
from apiCandidat.models import Candidat
from apiCandidat.models import Recruteur
from apiCandidat.models import Client
from apiCandidat.models import Partenaire
from apiCandidat.models import Offre
from apiCandidat.models import Meeting




class CandidatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidat
        fields = ['id', 'first_name', 'last_name', 'email', 'telephone','adress', 'resume']
class RecruteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruteur
        fields = ['id', 'first_name', 'last_name','entreprise', 'email', 'telephone', 'needed_profile', 'crenaux_proposé','appel_telephonique','piece_jointe']
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name','service', 'telephone','email', 'appel_telephonique','piece_jointe']
class PartenaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partenaire
        fields = ['id', 'first_name', 'last_name','type_partenariat', 'telephone','email' ,'appel_telephonique', 'date_crenaux','piece_jointe']
class OffreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offre
        fields = ['id','titre','category', 'description', 'salaire', 'entreprise','mode' ,'location']
class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = ['id','date','time_start', 'time_end','title', 'details']

