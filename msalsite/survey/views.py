from django.shortcuts import render
from .forms import SurveyForm

def poll_view(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            answer = form.cleaned_data['question']
            # You can save the answer to the database or process it as needed
            return render(request, 'survey/thanks.html', {'answer': answer})
        
    else:   
        form = SurveyForm()

    return render(request, 'survey/poll.html', {'form': form})
    

# Create your views here.
