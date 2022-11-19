#for all python function required
from __future__ import print_function

# from apiclient import discovery
# from httplib2 import Http
# from oauth2client import client, file, tools

# def get_form_responces():
#     SCOPES = "https://www.googleapis.com/auth/forms.responses.readonly"
#     DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

#     store = file.Storage('token.json')
#     creds = None
#     if not creds or creds.invalid:
#         flow = client.flow_from_clientsecrets('C:/Users/chinm/OneDrive/Desktop/5th sem/SE/PROJECT/client_secrets.json', SCOPES)
#         creds = tools.run_flow(flow, store)
#     service = discovery.build('forms', 'v1', http=creds.authorize(
#         Http()), discoveryServiceUrl=DISCOVERY_DOC, static_discovery=False)

#     # Prints the responses of your specified form:
#     form_id = '1fqGKaYTANP7zN5X1T85zndlHScajGkyOAqrj0q3bqUk'
#     result = service.forms().responses().list(formId=form_id).execute()
#     # print(type(result))
#     return result
