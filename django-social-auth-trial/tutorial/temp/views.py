from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    print(request.user)
    if request.user.is_authenticated:
        social = request.user.social_auth.get(provider='fitbit')
        token = social.extra_data['access_token']
        print(token)
    return render(request, 'temp/index.html')

# https://www.fitbit.com/oauth2/authorize?client_id=22D3H4&redirect_uri=http://localhost:8000/complete/fitbit/&state=dqOuEqrXhT7nxrTyxK0fpGvgOklUQDo2&response_type=code&scope=activity+heartrate+profile+sleep+weight+profile
