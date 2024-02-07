from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
def main(request):
    current_user = request.user
    user = User.objects.get(pk=current_user.id)
    title_ = "Main"
    data={
        'title':title_,
        'user':user
    }
    return render(request,'main/main.html',data)
def main_UID(request,ID):
    pass