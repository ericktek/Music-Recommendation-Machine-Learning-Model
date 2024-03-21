from django.http import JsonResponse
from django.shortcuts import render
from .forms import MusicGenreForm
import joblib
import json

def index(request):
    form = MusicGenreForm()
    return render(request, 'index.html', {'form': form})

def predict_genre(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        form = MusicGenreForm(request.POST)
        if form.is_valid():
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender']
            model = joblib.load('music-recommender.pkl')
            prediction = model.predict([[age, gender]])
            # Convert ndarray to a JSON serializable format
            prediction_json = prediction.tolist()  # Convert to Python list
            return JsonResponse({'result': prediction_json})
        else:
            return JsonResponse({'error': 'Form is not valid'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method or not an AJAX request'}, status=405)
