from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
# Create your views here.
from rest_framework import permissions
from .serializers import ContactSerializer
from .models import Contact 


class ContactListView(ListCreateAPIView):

    serializer_class=ContactSerializer
    permission_classes= (permissions.IsAuthenticated,)
    

    

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

      

    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user) 





class ContactDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class=ContactSerializer
    permission_classes= (permissions.IsAuthenticated,)

    lookup_field="id"

    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)            
