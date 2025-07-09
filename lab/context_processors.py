from django.conf import settings

def baseurl(request):
    return {'BASEURL': settings.BASEURL}