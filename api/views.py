from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from django.core.mail import send_mail

from .serializers import ClientEmailSerializer, TestimonialSerializer, AddressSerializer, PhoneSerializer, EmailSerializer, TeamSerializer, SocialSerializer, MissionSerializer, VisionSerializer, HomeVideoSerializer, RepliedEmailSerializer, EmailCountSerializer
from .models import ClientEmail, Testimonial, Address, Phone, Email, Team, Social, Mission, Vision, HomeVideo, EmailCount


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

        # qs.image = data.get('image', qs.image)
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
        qs.link = data.get('link', qs.link)
        qs.save()
        serializer = HomeVideoSerializer(qs)
        return Response(serializer.data)


@api_view(['GET'])
def getClientEmails(request):
    qs = ClientEmail.objects.all()
    serializer = ClientEmailSerializer(qs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getClientEmail(request, pk):
    qs = ClientEmail.objects.get(id=pk)
    serializer = ClientEmailSerializer(qs, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def addClientEmail(request):
    serializer = ClientEmailSerializer(data=request.data)
    emailData = request.data
    name = emailData.get('name')
    email = emailData.get('email')
    body = name + ' is enquiring about your services \nCheck their messages on your Dashboard'
    if serializer.is_valid():
        send_mail('FastD Enquiry Notification', body, 'malingreatsdev@gmail.com',
                  ['bennyakambangwe@gmail.com'], fail_silently=False)
        # send_mail('', body , 'malingreatsdev@gmail.com',
        #           ['bennyakambangwe@gmail.com'], fail_silently=False)
        serializer.save()
        query = EmailCount.objects.get(id=2)
        query.totalMail += 1
        query.save()
    else:
        return Response('serializer not valid')
    return Response(serializer.data)


@api_view(['POST'])
def ReplyEmail(request):
    serializer = RepliedEmailSerializer(data=request.data)
    emailData = request.data

    email = emailData.get('email')
    message = emailData.get('message')
    if serializer.is_valid():
        send_mail('Hello From FastD', message, 'malingreatsdev@gmail.com',
                  [email], fail_silently=False)
        serializer.save()
        pkey = emailData.get('pkey')
        qs = ClientEmail.objects.get(id=pkey)
        qs.answered = 'True'
        qs.save()
        print('Saved Email Client Update')
        query = EmailCount.objects.get(id=2)
        query.repliedMail += 1
        query.unrepliedMail -= 1
        query.save()
    else:
        return Response('serializer not valid')
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteClientEmail(request, pk):
    clientEmail = ClientEmail.objects.get(id=pk)
    clientEmail.delete()
    return Response('ClientEmail Deleted')


@api_view(['GET'])
def getEmailCount(request):
    qs = EmailCount.objects.get(id=2)
    serializer = EmailCountSerializer(qs, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def addEmailCount(request):
    serializer = EmailCountSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response('serializer not valid')
    return Response(serializer.data)


# class CustomerView(APIView):

# 	def post(self, request, *args, **kwargs):
# 		serializer = CustomerSerializer(data = request.data)
# 		if	serializer.is_valid():
# 			serializer.save()
# 			customer_data = serializer.data
# 			customer = Customer.objects.get(email=customer_data['email'])

# 			email_body = 'Someone Just Submitted a Form @malingreats.org \n\n\n NAME:		'+customer.name+'\n CITY:		'+customer.city+'\n EMAIL:		'+customer.email+'\n PHONE:		'+customer.phone+'\n COMPANY:	'+customer.company+'\n CHOICE:		'+customer.choice+'\n MESSAGE:	'+customer.themessage
# 			data={'email_body': email_body, 'subject': 'Potential Client'}
# 			Util.send_email(data)
# 			return Response(serializer.data)
# 		return Response(serializer.errors)


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        'api/token/refresh'
    ]

    return Response(routes)
