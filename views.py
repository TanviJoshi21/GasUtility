from django.shortcuts import render, redirect
from .models import ServiceRequest
from .forms import ServiceRequestForm

def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user
            service_request.save()
            return redirect('track_requests')
    else:
        form = ServiceRequestForm()
    return render(request, 'requests/submit_request.html', {'form': form})

def track_requests(request):
    requests = ServiceRequest.objects.filter(customer=request.user)
    return render(request, 'requests/track_requests.html', {'requests': requests})