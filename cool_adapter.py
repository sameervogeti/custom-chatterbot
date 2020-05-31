from chatterbot.logic import LogicAdapter
import spacy

class MyLogicAdapter(LogicAdapter):
 nlp = spacy.load("en_core_web_sm")
 def __init__(self, chatbot, **kwargs):
     super().__init__(chatbot, **kwargs)

 def can_process(self, statement):
     user_input = statement.text.lower()
     if 'weather' in user_input:
         return True
     else:
         return False

 def process(self, input_statement, additional_response_selection_parameters):
     from chatterbot.conversation import Statement
     doc = self.nlp(input_statement.text.lower())
     # Make a request to the temperature API
     # api-endpoint
     for ent in doc.ents:
         # Print the entity text and its label
         print(ent.text, ent.label_)
         if(ent.label_=="GPE"):
             data=self.find_weather(ent.text)
             # Let's base the confidence value on if the request was successful

             response_statement = Statement(data)
             response_statement.confidence=1
             return response_statement
     response_statement = Statement("No GPE found to query weather Data")
     response_statement.confidence = 1
     return response_statement
 @staticmethod
 def find_weather(city):
     from chatterbot.conversation import Statement
     import requests
     URL = "https://community-open-weather-map.p.rapidapi.com/weather"

     # location given here

     # defining a params dict for the parameters to be sent to the API
     PARAMS = {"q": city}

     HEADERS = {"x-rapidapi-host": "community-open-weather-map.p.rapidapi.com",
                "x-rapidapi-key": "2b57e58d9cmsh9b17b2536cbf8c6p12acc0jsna8e3b52625cb",
                "useQueryString": "true"}

     # sending get request and saving the response as response object
     response = requests.get(url=URL, headers=HEADERS, params=PARAMS)
     print(response.json())
     data = response.json()
     return data