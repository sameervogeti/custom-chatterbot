from chatterbot.logic import LogicAdapter


class MyLogicAdapter(LogicAdapter):

 def __init__(self, chatbot, **kwargs):
     super().__init__(chatbot, **kwargs)

 def can_process(self, statement):
     """
     Return true if the input statement contains
     'what' and 'is' and 'temperature'.
     """
     words = ['How', 'is', 'the','weather','in','London?']
     if all(x in statement.text.split() for x in words):
         return True
     else:
         return False

 def process(self, input_statement, additional_response_selection_parameters):
     from chatterbot.conversation import Statement
     import requests

     # Make a request to the temperature API
     # api-endpoint
     URL = "https://community-open-weather-map.p.rapidapi.com/weather"

     # location given here


     # defining a params dict for the parameters to be sent to the API
     PARAMS = {"q": "London,uk"}

     HEADERS = {"x-rapidapi-host": "community-open-weather-map.p.rapidapi.com",
	"x-rapidapi-key": "2b57e58d9cmsh9b17b2536cbf8c6p12acc0jsna8e3b52625cb",
	"useQueryString": "true"}

     # sending get request and saving the response as response object
     response = requests.get(url=URL,headers=HEADERS, params=PARAMS)
     print(response.json())
     data=response.json()
     # Let's base the confidence value on if the request was successful
     if response.status_code == 200:
         confidence = 1
     else:
         confidence = 0



     response_statement = Statement(data)
     response_statement.confidence = confidence
     return response_statement