from . import forms
from ProjectManager.settings import LOGIN_REDIRECT_URL
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
 
from core.models import CustomUser, Project, Permission, Role, ProjectType
from core.serializers import UserListSerializer, UserDetailSerializer, ProjectDetailSerializer, ProjectListSerializer, PermissionSerializer, RoleSerializer, ProjectTypeSerializer
# from django.http import HttpResponse


# Create your views here.
def logout_user(request):
    logout(request)
    return redirect('login')


class LoginPage(View):
    form_class = forms.LoginForm
    template_name = "core/login.html"

    def get(self, request):
        form = self.form_class()
        message = ''
        return render(
            request=request,
            template_name=self.template_name,
            context={'form': form, 'message': message}
        )

    def post(self, request):
        form = forms.LoginForm(request.POST)
        message = ''
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('feed')
        message = 'Identifiants invalides.'
        return render(
            request,
            self.template_name,
            context={'form': form, 'message': message}
        )


def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
                )
            if user is not None:
                login(request, user)
                return redirect('feed')
            else:
                message = 'Identifiants invalides.'
    return render(request, "core/login.html", context={'form': form, 'message': message})


def sign_up_page(request):
    form = forms.SignUpForm()
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(LOGIN_REDIRECT_URL)
    return render(request, "core/sign_up.html", context={'form': form})


class UserViewSet(ModelViewSet):
    serializer_class = UserListSerializer
    detail_serializer_class = UserDetailSerializer

    def get_queryset(self):
        return CustomUser.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()

class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectListSerializer
    detail_serializer_class = ProjectDetailSerializer

    def get_queryset(self):
        return Project.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()


class PermissionAPIView(APIView):
    def get(self, *args, **kwargs):
        permissions = Permission.objects.all()
        serializer = PermissionSerializer(permissions, many=True)
        return Response(serializer.data)


class RoleAPIView(APIView):
    def get(self, *args, **kwargs):
        roles = Role.objects.all()
        serializer = RoleSerializer(roles, many=True)
        return Response(serializer.data)


class ProjectTypeAPIView(APIView):
    def get(self, *args, **kwargs):
        project_types = ProjectType.objects.all()
        serializer = ProjectTypeSerializer(project_types, many=True)
        return Response(serializer.data)
