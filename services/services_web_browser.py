import os
import re
from googlesearch import search
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class WebBrowserServices:

    def __init__(self):
        self.chrome_driver_path = "C:/webdriver/chromedriver.exe"

    def open_browser(self, query):
        if query is not None:
            try:
                for j in search(query, num_results=1):
                    page_content = self.get_page_content(j)
                    if page_content is not None:
                        cleaned_content = self.remove_html_tags(page_content)
                        cleaned_content = self.remove_single_char_lines(cleaned_content)
                        print(f"open_browser {cleaned_content}")
                        limited_page_content = ' '.join(cleaned_content.split())
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

    def remove_html_tags(self, text):
        cleanr = re.compile('<.*?>')
        cleantext = re.sub(cleanr, '', text)
        return cleantext

    def remove_single_char_lines(self, text):
        lines = text.split("\n")
        cleaned_lines = [line for line in lines if len(line.strip()) > 2]
        return "\n".join(cleaned_lines)


