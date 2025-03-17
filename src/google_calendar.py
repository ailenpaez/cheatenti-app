import os
import json
import datetime
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

#Permisos accesos al calendar.

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly',]

def authenticate():
     """Auth to Google Calendar API."""
     creds= None
     
     if os.path.exist('token.json'): #buscar token
          creds = Credentials.from_authorized_user_info(
            json.loads(open('token.json', 'r').read()), SCOPES)