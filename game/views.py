from django.http import HttpResponse

def index(request):
    line1 = '<h1 style = "text-align: center"> 术士之战 </h1>'
    line2 = '<img src = "https://img.3dmgame.com/uploads/allimg/140323/235_140323205352_1_lit.jpg" width = 1800>'
    line3 = '<a href = "/play/", style = "text-align: center"> 进入游戏界面 </a>'
    return HttpResponse(line1 + line3 + line2)

def play(requst):
    line1 = '<h1 style = "text-align: center"> 游戏界面</h1>'
    line3 = '<a href = "/", style = "text-align: center"> 返回主界面 </a>'
    line2 = '<img src = "https://img.3dmgame.com/uploads/allimg/140323/235_140323205352_1_lit.jpg" width = 1800>'
    return HttpResponse(line1 + line3 + line2)
