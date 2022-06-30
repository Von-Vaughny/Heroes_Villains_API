from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from supers.models import Super
from supers.serializers import SuperSerializer


@api_view(['GET', 'POST'])
def supers_list(request):
    supers = Super.objects.all()
    custom_response = {}
    if request.method == 'GET':
        super_param_type = request.query_params.get('type')
        if super_param_type:
            supers = supers.filter(super_type_id__type=super_param_type)
        for super in supers:
            super_types = Super.objects.filter(super_type__type=super.super_type.type)
            serializer = SuperSerializer(super_types, many=True)
            custom_response[f'{super.super_type.type}{"es" if super.super_type.type=="Hero" else "s"}']=serializer.data
        return Response(custom_response, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def supers_detail(request, pk):
    super = Super.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = SuperSerializer(super)
        return Response(serializer.data, status=status.HTTP_200_OK)
