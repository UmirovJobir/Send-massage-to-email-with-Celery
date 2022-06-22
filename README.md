# Send-massage-to-email-with-Celery

1. first run server: python3 manage.py runserver

2. to activate worker, open a new terminal a put this command:
  celery -A sendemail worker -l INFO

3. to activate beat, open a new terminal a put this command:
  celery -A sendemail beat -l info
