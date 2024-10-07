import urllib.request
import json
import requests

class API:

    def for_senti(self, text):
       url = "https://api.apiverve.com/v1/sentimentanalysis"
       api_key = "your api key"
       headers = {
         "x-api-key": f"{api_key}",
         "Content-Type": "application/json",
         "Accept": "application/json",
         "User-Agent": "Mozilla/5.0 (Platform; RV:11.0) Gecko/20100101 Firefox/11.0"
       }
       payload = {"text": text}
       data = json.dumps(payload).encode()
       req = urllib.request.Request(url, data,headers)

       with urllib.request.urlopen(req) as response:
           response_data = response.read().decode()

       parsed_data = json.loads(response_data)
       sentiment_text = parsed_data["data"]["sentimentText"]
       return sentiment_text


    def emotions(self, text):
        url = "https://ekman-emotion-analysis.p.rapidapi.com/ekman-emotion"
        api_key = "your api key"
        payload = [
            {
                "id": "1",
                "language": "en",
                "text": text
            }
        ]

        headers = {
            "x-rapidapi-key": f"{api_key}",
            "x-rapidapi-host": "ekman-emotion-analysis.p.rapidapi.com",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        response = requests.post(url, json=payload, headers=headers)
        new_data = response.json()
        prediction_text = new_data[0]["predictions"][0]["prediction"]
        return prediction_text

    def ner(self, text):
        url = "https://namedentityextractor.p.rapidapi.com/linguistics/interpret-text"
        payload = {
            "analysisInput": {
                "documents": [
                    {
                        "id": 1,
                        "language": "en",
                        "text": text
                    }
                ]
            }
        }

        api_key = "your api key"

        headers = {
            "x-rapidapi-key": f"{api_key}",
            "x-rapidapi-host": "namedentityextractor.p.rapidapi.com",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0 (Platform; RV:11.0) Gecko/20100101 Firefox/11.0"
        }

        data = json.dumps(payload).encode()
        req = urllib.request.Request(url, data, headers)

        response = urllib.request.urlopen(req)
        new_data = response.read().decode()
        new_data = json.loads(new_data)

        for document in new_data.get("documents", []):
            for entity in document.get("entities", []):
                category = entity.get("category")
                entity_type = entity.get("type")
                return f"Category: {category}, Type: {entity_type}"






