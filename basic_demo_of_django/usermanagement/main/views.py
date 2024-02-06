from django.shortcuts import render

# Create your views here.
def main(request):
    title_ = "Main"
    data={
        'title':title_
    }
    return render(request,'main/main.html',data)
# name of postgres DB instance -> usermanagement
# DB pass -> Ilovewhitechicks@69