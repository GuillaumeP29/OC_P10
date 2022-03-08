from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
# from rest_framework.validators import UniqueValidator
# from django.contrib.auth.password_validation import validate_password

from core.models import CustomUser, Project, ProjectType, Contributor


class UserListSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name']


class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_superuser', 'is_staff', 'is_active']


# class RegisterUserSerializer(ModelSerializer):
#     email = serializers.EmailField(
#             required=True,
#             validators=[UniqueValidator(queryset=CustomUser.objects.all())]
#             )

#     password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
#     password2 = serializers.CharField(write_only=True, required=True)

#     class Meta:
#         model = CustomUser
#         fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
#         extra_kwargs = {
#             'first_name': {'required': True},
#             'last_name': {'required': True}
#         }

#     def validate(self, data):
#         if data['password'] != data['password2']:
#             raise serializers.ValidationError({"password": "Password fields didn't match."})

#         if CustomUser.objects.filter(first_name=data['first_name']).exists():
#             if CustomUser.objects.filter(last_name=data['last_name']).exists():
#                 raise serializers.ValidationError({"first_name / last_name": "Another user already has
# the same first name and last name"})

#         return data

#     def validate_username(self, value):
#         if CustomUser.objects.filter(username=value).exists():
#             raise serializers.ValidationError('Username already used')

#         return value

#     def create(self, validated_data):
#         user = CustomUser.objects.create(
#             username=validated_data['username'],
#             email=validated_data['email'],
#             first_name=validated_data['first_name'],
#             last_name=validated_data['last_name']
#         )

#         user.set_password(validated_data['password'])
#         user.save()
#         return user


class ProjectTypeNameSerializer(ModelSerializer):
    class Meta:
        model = ProjectType
        fields = ['name']


class ProjectListSerializer(ModelSerializer):
    type = ProjectTypeNameSerializer()

    class Meta:
        model = Project
        fields = ['id', 'title', 'type']


class ProjectListPostSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'type']

    def validate_title(self, value):
        if Project.objects.filter(title=value).exists():
            raise serializers.ValidationError('A project already has this title')
        return value


class ProjectDetailSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'type']

    def validate_title(self, value):
        if Project.objects.filter(title=value).exists():
            raise serializers.ValidationError('A project already has this title')
        return value


class ProjectTypeSerializer(ModelSerializer):
    class Meta:
        model = ProjectType
        fields = ['id', 'name']


class ContributorSerializer(ModelSerializer):
    class Meta:
        model = Contributor
        fields = ['id', 'user', 'project', 'role']
