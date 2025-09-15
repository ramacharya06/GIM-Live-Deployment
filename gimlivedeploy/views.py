from django.shortcuts import render
from .models import Vote
from .models import IPs

def get_client_ip(request):
    """Extract client IP address, even if behind proxy."""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]  # first IP in list
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def home(request):

    votes = Vote.objects.all()
    print([vote.gender for vote in votes])
    return render(request, 'voting.html', {'votes': votes, 'gender': ['M', 'F']})

def submit_vote(request):
    if request.method == 'POST':
        client_ip = get_client_ip(request)
        print(f"Client IP: {client_ip}")
        votes = request.POST
        if IPs.objects.filter(ip_address=client_ip).exists():
            return render(request, 'already_voted.html')
        else:
            new_ip = IPs(ip_address=client_ip)
            new_ip.save()
        # print(votes)
        for key, value in votes.items():
            if key == 'csrfmiddlewaretoken':
                continue
            gimvote = Vote.objects.get(id=value)
            gimvote.votes += 1
            gimvote.save()
        
        return render(request, 'thankyou.html')