import requests

class APICaller:

    def api_call_get(url, query_params):
        url = url + query_params
        response = requests.get(url)
        return response