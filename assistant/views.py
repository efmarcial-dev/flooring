from django.shortcuts import render
import openai
import os
import json
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

openai.api_key = settings.OPEN_API_KEY

@csrf_exempt
def chat_view(request):
    if request.method == 'post':
        try:
            data = json.loads(request.body)
            user_input = data.get("message", "")
            
            response = openai.ChatCompletion.create(
                model = 'gpt-3.5-turbo',
                message = [
                    {"role" : "system", "content" : "You area a help full assistant for a home service business."},
                    {"role" : "user", "content" : user_input}
                ]
            )
            
            reply = response.choices[0].message['content'].strip()
            return JsonResponse({"reply": reply})
        
        except Exception as e:
            return JsonResponse({"error" : str(e)}, status = 500)
        
    return JsonResponse({"error": "Invalid request"}, status = 400)