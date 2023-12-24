from django.shortcuts import render, redirect

# Create your views here.
'''
Vikraal 442
Rollex 997
Ballistic 117
Bullet 897
Barricade 4090
Barbatos 007
Endevour 380
Fury 787
Leo 747
LockDown 887
Dynamite 101
ShockWave 999
Blast 036
Ghost 002
Nightmare 597
Dispare 551
Hurricane 451
Cyclone 447
Xcalibur 1000
Saber 1007
SilverArrow 1017
Trident 990
Obsidian 001
Venom 097
Cobra 077
RedAlert 1080
Almight 3090
MahaKaal 051
Kailash 107
SideSwipe 111
Snipe 100
'''
def home(request):
    return render(request,'home.html')