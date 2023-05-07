import os
import re
from googlesearch import search
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from io import BytesIO
from pdfdocument.document import PDFDocument
import pdfkit
import uuid
from bs4 import BeautifulSoup

class WebBrowserServices:

    def __init__(self):
        self.chrome_driver_path = "C:/webdriver/chromedriver.exe"
        self.dir = "./data"

    def open_browser(self, query):
        if query is not None:
            try:
                for j in search(query, num_results=1):
                    html_page = self.get_page_content(j)
                    if html_page is not None:
                        html = self.save_html_to_file(html_page)
                        data = self.html_to_pdf(html)
                        return data
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

    def save_html_to_file(self, html_content, file_path='./html/data.html'):
        try:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            html_without_dependencies = self.remove_dependencies(html_content)
            return html_without_dependencies
        except Exception as e:
            print(f"Error al guardar el archivo HTML: {e}")

    def remove_dependencies(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')

        # Eliminar todos los elementos <script>
        for script in soup.find_all('script'):
            script.decompose()

        # Eliminar todos los elementos <link> con atributo rel="stylesheet"
        for link in soup.find_all('link', rel="stylesheet"):
            link.decompose()

        # Eliminar todos los elementos <style>
        for style in soup.find_all('style'):
            style.decompose()

        return str(soup)


    def html_to_pdf(self, html):
        # convertir html en pdf y guardar archivo en self.dir
        print("dentro html_to_pdf")
        try:
            # Crear un nombre único para el archivo PDF
            # pdf_file_name = f"{uuid.uuid4().hex}.pdf"
            pdf_file_path = "./data/data.pdf"
            # Configurar las opciones de PDF
            pdf_options = {
                'quiet': '',
                'page-size': 'Letter',
                'encoding': "UTF-8",
                'disable-smart-shrinking': '',
                'no-outline': None
            }

            # Convertir HTML a PDF usando pdfkit
            path_to_wkhtmltopdf = "C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe"
            config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)
            pdfkit.from_string(html, pdf_file_path, options=pdf_options, configuration=config)

            print(f"Archivo PDF guardado exitosamente en {pdf_file_path}")
            return pdf_file_path
        except Exception as e:
            print(f"Error al convertir el HTML a PDF: {e}")
            return None





