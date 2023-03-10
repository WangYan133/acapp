from django.http import HttpResponse

def index(request):
    line1 = '<h1 style = "text-align: center"> 术士之战 </h1>'
    line2 = '<img src = "https://img.3dmgame.com/uploads/allimg/140323/235_140323205352_1_lit.jpg" width = 1800>'
    return HttpResponse(line1 + line2)
