from rest_framework import serializers
from allauth.account.adapter import get_adapter
from .models import User, Profile, ProducerProfile
from rest_framework.authtoken.models import Token
from rest_auth.registration.serializers import RegisterSerializer
from categories.serializers import CategorySerializer



class ProducerProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProducerProfile
        fields = (
            'id',
            'first_name',
            'last_name',
            'profile_picture',
            'business_type',
            'company_name',
        )

class ProducerProfileDetailSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()


    class Meta:
        model = ProducerProfile
        fields = (
            'id',
            'user',
            'first_name',
            'first_name',
            'gender',
            'profile_picture',
            'province',
            'city',
            'company_name',
            'phone_numbner',
            'company_address',
            'office_address',
            'office_phone_num',
            'introduce_yourself',
            'description',
            'date_created_at',
            'web_site',
            'department',
            'job_title',
            'postal_code',
            'alternative_phone',
            'fax_number',
            'business_type',
            'category',
        )

    def get_category(self, obj):
        return CategorySerializer(obj.category).data

    def get_user(self, obj):
        return UserSerializer(obj.user).data

class ProfileDetailSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = (
            'id',
            'user',
            'first_name',
            'first_name',
            'gender',
            'profile_picture',
            'province',
            'city',
            'company_name',
            'phone_number',
            'company_address',
            'office_address',
            'office_phone_num',
            'introduce_yourself',
            'description',
            'date_created_at',
            'web_site',
        )

    def get_user(self, obj):
        return UserSerializer(obj.user).data

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = (
            'id',
            'first_name',
            'first_name',
            'gender',
            'profile_picture',
            'province',
            'city',
            'company_name',
            'phone_number',
            'company_address',
            'office_address',
            'office_phone_num',
            'introduce_yourself',
            'description',
            'date_created_at',
            'web_site',
        )



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'role')


class CustomRegisterSerializer(RegisterSerializer):
    ROLE_CHOICES = (
        ('خریدار', 'خریدار'),
        ('فروشنده', 'فروشنده'),
        ('هر دو', 'هر دو'),
    )
    role = serializers.ChoiceField(choices=ROLE_CHOICES)


    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'role')

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'role': self.validated_data.get('role', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.role = self.cleaned_data.get('role')
        user.save()
        adapter.save_user(request, user, self)
        return user



class TokenSerializer(serializers.ModelSerializer):
    user_role = serializers.SerializerMethodField()

    class Meta:
        model = Token
        fields = ('key', 'user', 'user_role')

    def get_user_role(self, obj):
        serializer_data = UserSerializer(obj.user).data
        role = serializer_data.get('role')
        return {
            'role': role,
        }
