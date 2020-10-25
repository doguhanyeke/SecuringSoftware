from django.http import HttpResponse
from .models import Message


# Create your views here.

def homePageView(request):
	idM = request.GET.get("id")
	print(idM)
	mes = Message.objects.get(id=idM);
	return HttpResponse(mes.content)
