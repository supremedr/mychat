web: daphne myChat.asgi:application --port $PORT --bind 0.0.0.0 -v2
chatworker: python manage.py runworker channels --settings=myChat.settings.railway -v2 
