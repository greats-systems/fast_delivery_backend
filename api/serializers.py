from rest_framework.serializers import ModelSerializer
from .models import ClientEmail, Testimonial, Address, Phone, Email, Team, Social, Mission, Vision, HomeVideo


class TestimonialSerializer(ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class PhoneSerializer(ModelSerializer):
    class Meta:
        model = Phone
        fields = '__all__'


class EmailSerializer(ModelSerializer):
    class Meta:
        model = Email
        fields = '__all__'


class TeamSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class SocialSerializer(ModelSerializer):
    class Meta:
        model = Social
        fields = '__all__'


class MissionSerializer(ModelSerializer):
    class Meta:
        model = Mission
        fields = '__all__'


class VisionSerializer(ModelSerializer):
    class Meta:
        model = Vision
        fields = '__all__'


class HomeVideoSerializer(ModelSerializer):
    class Meta:
        model = HomeVideo
        fields = '__all__'


class ClientEmailSerializer(ModelSerializer):
    class Meta:
        model = ClientEmail
        fields = '__all__'
