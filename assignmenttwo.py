class Request:
    def __init__(self, url):
        self.url = url

    def download_page(self):
        print(self.url)


class Website:
    def __init__(self, url, request_object):
        self.url = url
        self.request_object = request_object

    def website_title(self):
        self.request_object.download_page()
        return "My website title"


request = Request("www.youtube.com")
website = Website("www.youtube.com", request)
print(website.website_title())
