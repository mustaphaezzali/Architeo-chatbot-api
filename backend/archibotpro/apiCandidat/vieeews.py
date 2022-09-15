from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apiCandidat.models import Candidat
from apiCandidat.serializers import CandidatSerializer


@api_view(['GET', 'POST'])
def candidat_list(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        candidats = Candidat.objects.all()
        serializer = CandidatSerializer(candidats, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CandidatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'PUT', 'DELETE'])
def candidat_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        candidat = Candidat.objects.get(pk=pk)
    except Candidat.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CandidatSerializer(candidat)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Candidat(candidat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        candidat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


########################################################
#############################################
##############################$
from apiCandidat.models import Candidat
from apiCandidat.serializers import CandidatSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CandidatList(APIView):
    """
    List all candidats, or create a new snippet.
    """
    def get(self, request, format=None):
        candidats = Candidat.objects.all()
        serializer = CandidatSerializer(candidats, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CandidatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CandidatDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Candidat.objects.get(pk=pk)
        except Candidat.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        candidat = self.get_object(pk)
        serializer = CandidatSerializer(candidat)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        candidat = self.get_object(pk)
        serializer = CandidatSerializer(candidat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        candidat = self.get_object(pk)
        candidat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)