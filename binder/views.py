from django.shortcuts import render

# Create your views here.
def binder_view(request):
    """
    Renders the shop page with scheduled characters,
    combining model data, JSON metadata, and calculated
    attributes sorted by power.
    """
    page_url = "binder/binder.html"
    return render(request, page_url)