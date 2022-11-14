from knox.views import LoginView
from rest_framework.authentication import BasicAuthentication


class CustomLoginView(LoginView):
    authentication_classes = [BasicAuthentication]

