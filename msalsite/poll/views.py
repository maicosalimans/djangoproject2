from django.shortcuts import render
from .forms import PollForm

def poll_view(request):
    if request.method == 'POST':
        form = PollForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data
            answer = form.cleaned_data['question']
            #You can save the answer to the database or procedd it as needed
            return render(request, 'polls/thanks.html', {'answer': answer})
    else:
        form = PollForm()

    return render(request, 'pols/poll.html', {'form': form})

