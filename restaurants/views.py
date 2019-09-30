from django.shortcuts import render

# Create your views here.
def hi(request):
	context = {
	"msg": "Hello World!"
	}
	return render(request, 'hi.html', context)