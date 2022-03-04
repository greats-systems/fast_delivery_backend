from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from .serializers import TestimonialSerializer, AddressSerializer, PhoneSerializer, EmailSerializer, TeamSerializer, SocialSerializer, MissionSerializer, VisionSerializer, HomeVideoSerializer
from .models import Testimonial, Address, Phone, Email, Team, Social, Mission, Vision, HomeVideo


@api_view(['GET'])
def getTestimonials(request):
    qs = Testimonial.objects.all()
    serializer = TestimonialSerializer(qs, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addTestimonial(request):
    serializer = TestimonialSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response('serializer not valid')
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteTestimonial(request, pk):
    testimonial = Testimonial.objects.get(id=pk)
    testimonial.delete()
    return Response('Testimonial Deleted')


class PatchTestimonial(APIView):
    def patch(self, request, pk):
        qs = Testimonial.objects.get(id=pk)
        data = request.data

        qs.image = data.get('image', qs.image)
        qs.name = data.get('name', qs.name)
        qs.company = data.get('company', qs.company)
        qs.text = data.get('text', qs.text)
        qs.rating = data.get('rating', qs.rating)
        qs.save()
        serializer = TestimonialSerializer(qs)
        return Response(serializer.data)


@api_view(['GET'])
def getAddresses(request):
    qs = Address.objects.all()
    serializer = AddressSerializer(qs, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addAddress(request):
    serializer = AddressSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response('serializer not valid')
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteAddress(request, pk):
    address = Address.objects.get(id=pk)
    address.delete()
    return Response('Address Deleted')


class PatchAddress(APIView):
    def patch(self, request, pk):
        qs = Address.objects.get(id=pk)
        data = request.data

        qs.name = data.get('name', qs.name)
        qs.field1 = data.get('field1', qs.field1)
        qs.field2 = data.get('field2', qs.field2)
        qs.field3 = data.get('field3', qs.field3)
        qs.save()
        serializer = AddressSerializer(qs)
        return Response(serializer.data)


@api_view(['GET'])
def getPhone(request):
    qs = Phone.objects.all()
    serializer = PhoneSerializer(qs, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addPhone(request):
    serializer = PhoneSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response('serializer not valid')
    return Response(serializer.data)


@api_view(['DELETE'])
def deletePhone(request, pk):
    phone = Phone.objects.get(id=pk)
    phone.delete()
    return Response('Phone Deleted')


class PatchPhone(APIView):
    def patch(self, request, pk):
        qs = Phone.objects.get(id=pk)
        data = request.data

        qs.name = data.get('name', qs.name)
        qs.number = data.get('number', qs.number)
        qs.save()
        serializer = PhoneSerializer(qs)
        return Response(serializer.data)


@api_view(['GET'])
def getEmail(request):
    qs = Email.objects.all()
    serializer = EmailSerializer(qs, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addEmail(request):
    serializer = EmailSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response('serializer not valid')
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteEmail(request, pk):
    email = Email.objects.get(id=pk)
    email.delete()
    return Response('Email Deleted')


class PatchEmail(APIView):
    def patch(self, request, pk):
        qs = Email.objects.get(id=pk)
        data = request.data

        qs.name = data.get('name', qs.name)
        qs.email = data.get('email', qs.email)
        qs.save()
        serializer = EmailSerializer(qs)
        return Response(serializer.data)


@api_view(['GET'])
def getTeam(request):
    qs = Team.objects.all()
    serializer = TeamSerializer(qs, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addTeam(request):
    serializer = TeamSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response('serializer not valid')
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteTeam(request, pk):
    team = Team.objects.get(id=pk)
    team.delete()
    return Response('Team Deleted')


class PatchTeam(APIView):
    def patch(self, request, pk):
        qs = Team.objects.get(id=pk)
        data = request.data

        qs.name = data.get('name', qs.name)
        qs.title = data.get('title', qs.title)
        qs.image = data.get('image', qs.image)
        qs.save()
        serializer = TeamSerializer(qs)
        return Response(serializer.data)


@api_view(['GET'])
def getSocial(request):
    qs = Social.objects.all()
    serializer = SocialSerializer(qs, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addSocial(request):
    serializer = SocialSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response('serializer not valid')
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteSocial(request, pk):
    social = Social.objects.get(id=pk)
    social.delete()
    return Response('Social Deleted')


class PatchSocial(APIView):
    def patch(self, request, pk):
        qs = Social.objects.get(id=pk)
        data = request.data

        qs.facebook = data.get('facebook', qs.facebook)
        qs.twitter = data.get('twitter', qs.twitter)
        qs.linkedIn = data.get('linkedIn', qs.linkedIn)
        qs.whatsapp = data.get('whatsapp', qs.whatsapp)
        qs.save()
        serializer = SocialSerializer(qs)
        return Response(serializer.data)


@api_view(['GET'])
def getMission(request):
    qs = Mission.objects.all()
    serializer = MissionSerializer(qs, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addMission(request):
    serializer = MissionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response('serializer not valid')
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteMission(request, pk):
    mission = Mission.objects.get(id=pk)
    mission.delete()
    return Response('Mission Deleted')


class PatchMission(APIView):
    def patch(self, request, pk):
        qs = Mission.objects.get(id=pk)
        data = request.data

        qs.name = data.get('name', qs.name)
        qs.text = data.get('text', qs.text)
        qs.save()
        serializer = MissionSerializer(qs)
        return Response(serializer.data)


@api_view(['GET'])
def getVision(request):
    qs = Vision.objects.all()
    serializer = VisionSerializer(qs, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addVision(request):
    serializer = VisionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response('serializer not valid')
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteVision(request, pk):
    vision = Vision.objects.get(id=pk)
    vision.delete()
    return Response('Vision Deleted')


class PatchVision(APIView):
    def patch(self, request, pk):
        qs = Vision.objects.get(id=pk)
        data = request.data

        qs.name = data.get('name', qs.name)
        qs.text = data.get('text', qs.text)
        qs.save()
        serializer = VisionSerializer(qs)
        return Response(serializer.data)


@api_view(['GET'])
def getHomeVideo(request):
    qs = HomeVideo.objects.all()
    serializer = HomeVideoSerializer(qs, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addHomeVideo(request):
    serializer = HomeVideoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response('serializer not valid')
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteHomeVideo(request, pk):
    homeVideo = HomeVideo.objects.get(id=pk)
    homeVideo.delete()
    return Response('HomeVideo Deleted')


class PatchHomeVideo(APIView):
    def patch(self, request, pk):
        qs = HomeVideo.objects.get(id=pk)
        data = request.data

        qs.title = data.get('title', qs.title)
        qs.text = data.get('text', qs.text)
        qs.video = data.get('video', qs.video)
        qs.save()
        serializer = HomeVideoSerializer(qs)
        return Response(serializer.data)


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        'api/token/refresh'
    ]

    return Response(routes)
