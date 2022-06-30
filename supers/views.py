from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from supers.models import Super
from supers.serializers import SuperSerializer


@api_view(['GET'])
def supers_list(request):
    supers = Super.objects.all()
    custom_response = {}
    if request.method == 'GET':
        super_param_type = request.query_params.get('type')
        if super_param_type:
            supers = supers.filter(super_type__type=super_param_type)
        for super in supers:
            super_types = Super.objects.filter(super_type__type=super.super_type.type)
            serializer = SuperSerializer(super_types, many=True)
            custom_response[super.super_type.type]=serializer.data
    return Response(custom_response, status=status.HTTP_200_OK)



#@api_view(['GET'])
#def super_detail(request, pk):
#    super = Super.objects.get(pk=pk)
#    if request.method == 'GET':
#        serializer = SuperSerializer(super)
#        return Response(serializer.data)
