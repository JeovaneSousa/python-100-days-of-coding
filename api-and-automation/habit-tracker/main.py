import requests
import datetime as dt

TOKEN = "abcjsdf1aasd234lk"
USERNAME = "jeovabarbosa"
BASE_URL = "https://pixe.la/v1/users"
HEADER = {
    "X-USER-TOKEN": TOKEN
}

def create_acount():
    body = {
    "token": "abcjsdf1aasd234lk",
    "username":"jeovabarbosa",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
  
    response = requests.post(url=BASE_URL, json=body)
    error = response.raise_for_status()
    print(response.text)

# create_acount()

def craete_graph(id, name, unit, type, color): 
    endpoint = f"{BASE_URL}/{USERNAME}/graphs"

    body = {
        "id":id,
        "name":name,
        "unit": unit,
        "type": type,
        "color": color
    }

    response = requests.post(url=endpoint, json=body, headers=HEADER)
    response.raise_for_status()
    print(response.text)

# craete_graph (
#     id="pagecount2023",
#     name="Reading Progress",
#     unit="pages",
#     type="int",
#     color="kuro"
# )

def get_graph_url_with_id(graph_id:str) -> None:
    endpoint = f"{BASE_URL}/{USERNAME}/graphs/{graph_id}.html"
    print(endpoint)

def add_pixel(graph_id: str, page_number:int) -> None:
    endpoint = f"{BASE_URL}/{USERNAME}/graphs/{graph_id}"
    today = dt.datetime.now()
    date_formated = today.strftime("%Y%m%d")

    body = {
        "date":date_formated,
        "quantity": str(page_number)
    }

    response = requests.post(url=endpoint, headers=HEADER, json=body)
    response.raise_for_status()
    print(response.text)


    

get_graph_url_with_id(graph_id="pagecount2023")

add_pixel("pagecount2023", page_number=10)