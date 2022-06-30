from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from super_types.models import SuperType
from super_types.serializers import SuperTypeSerializer


@api_view(['GET', 'POST'])
def super_types_list(request):
    super_types = SuperType.objects.all()
    if request.method == 'GET':
        serializer = SuperTypeSerializer(super_types, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'POST':
        serializer = SuperTypeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def super_types_detail(request, pk):
    super_type = SuperType.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = SuperTypeSerializer(super_type)
        return Response(serializer.data, status=status.HTTP_200_OK)
