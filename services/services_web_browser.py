# from googlesearch import search
# import requests
# from bs4 import BeautifulSoup
# from operator import itemgetter
#
# class WebBrowserServices:
#
#     def open_browser(self, query):
#         if query is not None:
#             try:
#                 for j in search(query, num_results=1):
#                     soup = self.get_page_content(j)
#                     if soup is not None:
#                         page_content = ' '.join(soup.stripped_strings)
#                         print(f" open_browser {page_content}")
#                         limited_page_content = ' '.join(page_content.split())
#                         return limited_page_content
#
#                     break
#             except Exception as e:
#                 print("Error al realizar la búsqueda:", e)
#         return None
#
#
#     def get_page_content(self, url):
#         try:
#             response = requests.get(url)
#             response.raise_for_status()
#             soup = BeautifulSoup(response.text, 'html.parser')
#             return soup
#         except requests.exceptions.HTTPError as e:
#             print(f"Error al obtener la página: {e}")
#             return None
#
#
#
from googlesearch import search
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

class WebBrowserServices:

    def __init__(self):
        self.chrome_driver_path = "C:/webdriver/chromedriver.exe"

    def open_browser(self, query):
        if query is not None:
            try:
                for j in search(query, num_results=1):
                    page_content = self.get_page_content(j)
                    if page_content is not None:
                        print(f"open_browser {page_content}")
                        limited_page_content = ' '.join(page_content.split())
                        return limited_page_content

                    break
            except Exception as e:
                print("Error al realizar la búsqueda:", e)
        return None

    def get_page_content(self, url):
        try:
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            driver = webdriver.Chrome(executable_path=self.chrome_driver_path, options=chrome_options)
            driver.get(url)
            page_content = driver.page_source
            driver.quit()
            return page_content
        except Exception as e:
            print(f"Error al obtener la página: {e}")
            return None
