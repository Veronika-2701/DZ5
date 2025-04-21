import requests
import pytest
from tests.yougile import YouGile

ratata = YouGile("https://ru.yougile.com/api-v2/")

def test_get_list_proj():
    assert ratata.req_get('GET','projects/91bcbcda-09ef-4cbe-8d42-efff443c620f').status_code == 200
    assert ratata.req_get('GET','projects/91bcbcda-09ef-4cbe-8d42-efff443c620x').status_code == 404
    PROJ_RESP = ratata.req_get('POST','projects',{
        "title": "Мой проект!",
        "users": {
            "5470f424-e2fd-4b8c-8e0f-01387924a5c3": "admin"
        }
        })
    assert PROJ_RESP.status_code == 201
    assert ratata.req_get('POST','projects',{
        "title": "Мой проект!",
        "users": {
            "5470f424-e2fd-4b8c-8e0f-": "admin"
        }
        }).status_code == 400
    assert ratata.req_get('PUT','projects/'+PROJ_RESP.json()["id"],{
        "deleted": False,
        "title": "Мой проектик!",
        "users": {
            "5470f424-e2fd-4b8c-8e0f-01387924a5c3": "admin"
        }
        }).status_code == 200
    assert ratata.req_get('PUT','projects/'+PROJ_RESP.json()["id"]+'gvhjn',{
        "deleted": False,
        "title": "Мой проектик!",
        "users": {
            "5470f424-e2fd-4b8c-8e0f-01387924a5c3": "admin"
        }
        }).status_code == 404
   
    
#dd08eb27-d13b-4e63-8ba6-8155ff0c0f66
