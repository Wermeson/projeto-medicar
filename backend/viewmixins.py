from rest_framework.views import APIView
from .models import Especialidade
from backend.api.serializers import EspecialidadeSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


class EspecialidadeReadViewMixin(APIView):
    def get(self, request, format=None):
        especialidades = Especialidade.objects.filter(ativo=True)
        serializer = EspecialidadeSerializer(especialidades, many=True)
        return Response(serializer.data)

    def post(self, request, pk=None):
        serializer = EspecialidadeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EspecialidadeViewMixin(APIView):
    def get_object(self, pk):
        try:
            return Especialidade.objects.get(id=pk)
        except Especialidade.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk is None:
            especialidades = Especialidade.objects.filter()
        else:
            especialidades = Especialidade.objects.filter(id=pk)
        serializer = EspecialidadeSerializer(especialidades, many=True)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk")
        especialidade = self.get_object(pk)
        serializer = EspecialidadeSerializer(especialidade, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk")
        especialidade = self.get_object(pk)
        serializer = EspecialidadeSerializer(
            especialidade, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, pk=None):
        serializer = EspecialidadeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
