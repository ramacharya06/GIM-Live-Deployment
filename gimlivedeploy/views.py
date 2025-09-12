from django.shortcuts import render
from .models import Vote



def home(request):

    votes = Vote.objects.all()
    print([vote.gender for vote in votes])
    return render(request, 'voting.html', {'votes': votes, 'gender': ['M', 'F']})

def submit_vote(request):
    if request.method == 'POST':
        votes = request.POST
        # print(votes)
        for key, value in votes.items():
            if key == 'csrfmiddlewaretoken':
                continue
            gimvote = Vote.objects.get(id=value)
            gimvote.votes += 1
            gimvote.save()
        
        return render(request, 'thankyou.html')