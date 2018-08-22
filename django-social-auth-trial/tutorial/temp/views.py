from django.shortcuts import render

# Create your views here.


def index(request):
    print(request.user)

    return render(request, 'temp/index.html')

# https://www.fitbit.com/oauth2/authorize?client_id=22D3H4&redirect_uri=http://localhost:8000/complete/fitbit/&state=dqOuEqrXhT7nxrTyxK0fpGvgOklUQDo2&response_type=code&scope=activity+heartrate+profile+sleep+weight+profile
