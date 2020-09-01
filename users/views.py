import json

from .models import ProducerProfile, Profile
from .forms import ProducerProfileForm, CustomerProfileForm
from django.shortcuts import render, redirect

from django.http import JsonResponse

from products.models import Product

from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from rest_framework import  status
from .serializers import ProducerProfileSerializer, ProfileSerializer, ProducerProfileDetailSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView,
    UpdateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView,
)
from rest_framework.views import APIView
from django.contrib.auth import login
from rest_auth.registration import views

from .permissions import IsOwnerOrReadOnly, IsProducer
"""
################################################################
            ##          ############         ##
           ## #         ##        ##         ##
          ##   #        ##        ##         ##
         ##     #       ##        ##         ##
        ## # # # #      ############         ##
       ##         #     ##                   ##
      ##           #    ##                   ##
     ##             #   ##                   ##
##################################################################      
"""

class UserIDView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({'userID': request.user.id}, status=status.HTTP_200_OK)


class ProducerProfileRUDView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProducerProfileSerializer
    lookup_field = 'pk'
    # permission_classes = (IsAuthenticated, IsOwnerOrReadOnly, IsProducer)

    def get_queryset(self):
        user = self.request.user
        qs = ProducerProfile.objects.all()
        return qs.filter(user=user)

class ProfileRUDView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    # lookup_field = 'pk'
    # permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    def get_queryset(self):
        username = self.kwargs['username']
        return Profile.objects.filter(user__username=username)

class ProfileCreateView(RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated,]
    serializer_class = ProfileSerializer

    def get_object(self):
        try:
            profile = Profile.objects.get(user=self.request.user)
            return profile
        except ObjectDoesNotExist:
            return Response({"message": "You do not have an active order"}, status=status.HTTP_400_BAD_REQUEST)



class ProducerProfileCreateView(CreateAPIView):
    # permission_classes = [IsAuthenticated, IsOwnerOrReadOnly, IsProducer]
    serializer_class = ProducerProfileDetailSerializer
    queryset = ProducerProfile.objects.all()


def sing_up(request):

    return render(request, 'views/signup.html', {})

"""
END OF:
################################################################
            ##          ############         ##
           ## #         ##        ##         ##
          ##   #        ##        ##         ##
         ##     #       ##        ##         ##
        ## # # # #      ############         ##
       ##         #     ##                   ##
      ##           #    ##                   ##
     ##             #   ##                   ##
##################################################################      
"""

def complete_prod_profile(request):
    producer = ProducerProfile.objects.get(user=request.user)
    form = ProducerProfileForm(instance=producer)
    if request.method == "POST":
        form = ProducerProfileForm(request.POST, instance=producer)
        if form.is_valid():
            gender = json.loads(request.POST['gender'])
            profile_picture = json.loads(request.POST['profile_picture'])
            province = json.loads(request.POST['province'])
            city = json.loads(request.POST['city'])
            company_name = json.loads(request.POST['company_name'])
            phone_number = json.loads(request.POST['phone_number'])
            company_address = json.loads(request.POST['company_address'])
            office_address = json.loads(request.POST['office_address'])
            office_phone_num = json.loads(request.POST['office_phone_num'])
            introduce_yourself = json.loads(request.POST['introduce_yourself'])
            description = json.loads(request.POST['description'])
            web_site = json.loads(request.POST['web_site'])
            categoty = json.loads(request.POST['categoty'])
            department = json.loads(request.POST['department'])
            job_title = json.loads(request.POST['job_title'])
            postal_code = json.loads(request.POST['postal_code'])
            alternative_phone = json.loads(request.POST['alternative_phone'])
            fax_number = json.loads(request.POST['fax_number'])
            business_type = json.loads(request.POST['business_type'])



            return redirect('/products/')
    context = { 'form' : form }
    return render(request, 'complete_prod_prof.html', context)


def customer_profile_completion(request):
    try:
        profile = Profile.objects.get(user=request.user)
        form = CustomerProfileForm(instance=profile)
        if request.method == "POST":
            form = CustomerProfileForm(request.POST, instance=profile)
            if form.is_valid():
                form.save()
                return redirect('users/profile')
        context = {
            'form': form,
        }
        return render(request, 'complete_customer_profile.html', context)

    except ObjectDoesNotExist:
        return Http404("not found")