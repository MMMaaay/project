from django.http import HttpResponse
from django.shortcuts import render
from . import model

def risk_form(request):
    return render(request, 'form.html')
 

def get_risk(request):  
    request.encoding='utf-8'
    feat = []
    if 'c1' in request.GET and request.GET['c1']:
        feat.append(int(request.GET['c1']))
    else:
        feat.append(0)
    if 'c2' in request.GET and request.GET['c2']:
        feat.append(int(request.GET['c2']))
    else:
        feat.append(0)
    if 'c3' in request.GET and request.GET['c3']:
        feat.append(int(request.GET['c3']))
    else:
        feat.append(0)
    if 'c4' in request.GET and request.GET['c4']:
        feat.append(int(request.GET['c4']))
    else:
        feat.append(0)
    if 'c5' in request.GET and request.GET['c5']:
        feat.append(int(request.GET['c5']))
    else:
        feat.append(0)
    if 'c6' in request.GET and request.GET['c6']:
        feat.append(int(request.GET['c6']))
    else:
        feat.append(0)
    if 'c7' in request.GET and request.GET['c7']:
        feat.append(int(request.GET['c7']))
    else:
        feat.append(0)
    if 'c8' in request.GET and request.GET['c8']:
        feat.append(int(request.GET['c8']))
    else:
        feat.append(0)
    if 'c9' in request.GET and request.GET['c9']:
        feat.append(float(request.GET['c9']))
    else:
        feat.append(0)
    if 'c10' in request.GET and request.GET['c10']:
        feat.append(int(request.GET['c10']))
    else:
        feat.append(0)
    if 'c11' in request.GET and request.GET['c11']:
        feat.append(int(request.GET['c11']))
    else:
        feat.append(0)
    if 'c12' in request.GET and request.GET['c12']:
        feat.append(int(request.GET['c12']))
    else:
        feat.append(0)
    if 'c13' in request.GET and request.GET['c13']:
        feat.append(int(request.GET['c13']))
    else:
        feat.append(0)
    message = ""
    risk = 0
    risk = dot(feat,weights)
    if (risk>0):
        message = "risk: high   " + "quote:$" + str(models.ProductContract.objects.values('AnnualizePremium').get(RiskLevel=1))
    else:
        message = "risk: low   " + "quote:$" + str(models.ProductContract.objects.values('AnnualizePremium').get(RiskLevel=1))
    return HttpResponse(message)