from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import Link
from django.http import HttpResponseRedirect

def scrape(request):
    if request.method == "POST":
        site = request.POST.get('site', '')

        if not site:
            return render(request, 'myapp/result.html', {'error': 'No site URL provided.'})

        try:
            page = requests.get(site)
            page.raise_for_status()  # Raises an HTTPError for bad responses
            soup = BeautifulSoup(page.text, 'html.parser')

            # Optional: Clear existing links to refresh the list
            Link.objects.all().delete()

            for link in soup.find_all('a'):
                link_address = link.get('href')
                link_text = link.string
                if link_address:  # Ensure link_address is not None
                    Link.objects.get_or_create(address=link_address, name=link_text)

        except requests.RequestException as e:
            return render(request, 'myapp/result.html', {'error': f'Error fetching the site: {e}'})

        return HttpResponseRedirect('/')

    else:
        data = Link.objects.all()
        return render(request, 'myapp/result.html', {'data': data})


def clear(request):
    Link.objects.all().delete()
    return render(request,'myapp/result.html')