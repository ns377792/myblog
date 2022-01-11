from django.shortcuts import redirect, render
from .models import Page
from blog.views import baseData
# Create your views here.
def page(request, page):
    pagedata = Page.objects.filter(url = page).first()
    if pagedata is not None:
        context = {
            "page":pagedata,
            "navThemeBar":baseData(),
        }
        return render(request, "pages/page.html", context)
    else:
        return redirect("/")