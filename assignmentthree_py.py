import requests
from bs4 import BeautifulSoup
class MainRequest:
    def __init__(self, url):
        self.url = url

    def download_page(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.find('title').text
            return title
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None


class Request(MainRequest):
    def __init__(self, url):
        super().__init__(url)

    def website_title(self, use_internet):
        if use_internet:
           return self.download_page()
        else:
            return "My website title"


# class Website:
#     def __init__(self, url, request_object):
#         self.url = url
#         self.request_object = request_object




request = Request("https://www.youtube.com/")
print(request.website_title(use_internet=True))
print(request.website_title(use_internet=False))
# website = Website("www.youtube.com", request)
# print(website.website_title())