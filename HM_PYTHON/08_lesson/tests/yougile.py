import requests

class YouGile:
    def __init__(self, base_url) -> None:
        self.base_url = base_url
        self.token = 'токен '

    def req_get(self, req_type="GET", url="", data={}):
        headers = {'Authorization': 'Bearer '+ self.token, 'Accept': 'application/json'}
    #    return requests.get(self.base_url + 'projects/'+id, headers=headers)
        return requests.request(req_type, self.base_url + url, headers=headers, json=data)
    
    def req_post(self, req_type="POST", url="", data={}):
        headers = {'Authorization': 'Bearer '+ self.token, 'Accept': 'application/json'}
        return requests.request(req_type, self.base_url + url, headers=headers, json=data)
    
    def req_put(self, req_type="PUT", url="", data={}):
        headers = {'Authorization': 'Bearer '+ self.token, 'Accept': 'application/json'}
        return requests.request(req_type, self.base_url + url, headers=headers, json=data)
    