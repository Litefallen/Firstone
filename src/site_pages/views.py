from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def some_view(request,*args,**kwargs):
    # return HttpResponse('<h3>This is default page</h3>')
    return render(request, 'home.html',{})

def contact_view(request,*args,**kwargs):
    # return HttpResponse('<h3>This is contacts page</h3>')
    return render(request, 'contacts.html',{})


def about_view(request, *args, **kwargs):
    return render(request,'about.html')
