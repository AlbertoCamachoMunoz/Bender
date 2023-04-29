from googlesearch import search
import requests
from bs4 import BeautifulSoup
from operator import itemgetter

class WebBrowserServices:

    def open_browser(self, query):
        if query is not None:
            try:
                for j in search(query, num_results=1):
                    soup = self.get_page_content(j)
                    if soup is not None:
                        page_content = ' '.join(soup.stripped_strings)
                        print(f" open_browser {page_content}")
                        limited_page_content = ' '.join(page_content.split())
                        return limited_page_content

                    break
            except Exception as e:
                print("Error al realizar la búsqueda:", e)
        return None


    def get_page_content(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            return soup
        except requests.exceptions.HTTPError as e:
            print(f"Error al obtener la página: {e}")
            return None



