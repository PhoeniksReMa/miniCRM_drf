from rest_framework import generics, viewsets, request
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Contact, Deal, Stage, Funnel
from .serializers import *


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (IsAuthenticated, )


class DealViewSet(viewsets.ModelViewSet):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer
    permission_classes = (IsAuthenticated,)


class StageViewSet(viewsets.ModelViewSet):
    queryset = Stage.objects.all()
    serializer_class = StageSerializer
    permission_classes = (IsAuthenticated,)

class FunnelViewSet(viewsets.ModelViewSet):
    queryset = Funnel.objects.all()
    serializer_class = FunnelSerializer
    permission_classes = (IsAuthenticated,)


# class ContactAPIList(generics.ListCreateAPIView):
#     queryset = Contact.objects.all()
#     serializer_class = ContactSerializer
#
# class ContactAPIUpdate(generics.UpdateAPIView):
#     queryset = Contact.objects.all()
#     serializer_class = ContactSerializer
#
# class ContactAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Contact.objects.all()
#     serializer_class = ContactSerializer


# class ContactAPIView(APIView):
#     def get(self, request):
#         queryset = Contact.objects.all()
#         return Response({'contacts': ContactSerializer(queryset, many=True).data})
#
#     def post(self, request):
#         serializer = ContactSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         post_new = Contact.objects.create(
#             name = request.data['name'],
#             phone = request.data['phone'],
#             email = request.data['email'],
#             adress = request.data['adress'],
#             deal = request.data.get('deal', None)
#         )
#         return Response({'post': ContactSerializer(post_new).data})