from django.shortcuts import render
from django.http import JsonResponse
import openai

# openai_api_key = 'key'
openai_api_key = 'key'
openai.api_key = openai_api_key

def ask_openai(message):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=message,
        max_tokens=150,
        stop=None,
    )
    answer = response.choices[0].text.strip()
    return answer

# Create your views here.
def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        return JsonResponse({'message' : message, 'response': response})
    return render(request, 'chatbot.html')