#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "25712887"))
API_HASH = environ.get("API_HASH", "e63bb82b544af7426b29d62939d99292")
BOT_TOKEN = environ.get("BOT_TOKEN", "7860223453:AAHvXa1pmrMI623LB0Eo2u6R1gThkQpLxHk")
OWNER = int(environ.get("OWNER", "1919432812"))
CREDIT = environ.get("CREDIT", "SURAJ YADAV")
AUTH_USER = os.environ.get('AUTH_USERS', '1919432812').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
