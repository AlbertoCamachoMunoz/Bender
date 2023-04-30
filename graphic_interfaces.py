import contextlib
import io
import os
import tkinter as tk

from PIL import ImageTk, Image
class GraphicInterfaces:

    def __init__(self, app_controller):
        self.app_controller = app_controller
        self.max_token = 2000
        self.page_content = ""
        self.input_width = 100  # Ajusta el valor según el ancho del botón

        # Crea la ventana principal
        self.windows = tk.Tk()
        self.windows.title("Si en tu viaje oyes la voz del lado oscuro, no dudes en acudir a mí")

        # Logo en la esquina superior izquierda
        image = Image.open("img/bender.jpg")
        resized_image = image.resize((150, 200), Image.ANTIALIAS)
        self.logo = ImageTk.PhotoImage(resized_image)
        self.logo_label = tk.Label(self.windows, image=self.logo)
        self.logo_label.grid(row=0, column=0, sticky='ew', padx=(10, 10), pady=(0, 0), rowspan=2)

        # Crea el cuadro de texto para ingresar el mensaje
        self.entry_message = tk.Entry(self.windows, width=self.input_width)
        self.entry_message.grid(row=0, column=1, sticky='ew', padx=(10, 5))

        # Crea el botón para enviar la pregunta
        self.btn_send = tk.Button(self.windows, text="Buscar URL", command=self.find_in_browser)
        self.btn_send.grid(row=0, column=2, sticky='e', padx=(5, 10))

        # Crea la caja de texto y la barra de desplazamiento para mostrar el resultado
        self.text_result = tk.Text(self.windows, height=10)  # Ajuste de la altura
        self.scrollbar_result = tk.Scrollbar(self.windows, command=self.text_result.yview)
        self.text_result.config(yscrollcommand=self.scrollbar_result.set)
        self.text_result.grid(row=1, column=1, columnspan=2, padx=10, pady=10, sticky='nsew')
        self.scrollbar_result.grid(row=1, column=3, sticky='ns', pady=10)

        # Permite que los widgets se ajusten al cambiar el tamaño de la ventana
        self.windows.columnconfigure(1, weight=1)
        self.windows.rowconfigure(1, weight=1)

        # Ejecuta el bucle principal de la ventana
        self.windows.mainloop()

    def create_chatgpt_interface(self):
        # Crea el cuadro de texto para ingresar la pregunta a ChatGPT
        self.entry_chatgpt_question = tk.Entry(self.windows, width=self.input_width)
        self.entry_chatgpt_question.grid(row=2, column=1, sticky='ew', padx=(10, 5))
        # self.entry_message.grid(row=0, column=1, sticky='ew', padx=(10, 5))

        # Crea el botón para enviar la pregunta a ChatGPT
        self.btn_send_chatgpt = tk.Button(self.windows, text="Preguntar a ChatGPT", command=self.send_chatgpt_question)
        self.btn_send_chatgpt.grid(row=2, column=2, sticky='e', padx=(15, 15))

        # Crea la caja de texto y la barra de desplazamiento para mostrar la respuesta de ChatGPT
        self.text_chatgpt_result = tk.Text(self.windows)
        self.scrollbar_chatgpt = tk.Scrollbar(self.windows, command=self.text_chatgpt_result.yview)
        self.text_chatgpt_result.config(yscrollcommand=self.scrollbar_chatgpt.set)
        self.text_chatgpt_result.grid(row=3, column=1, columnspan=2, padx=10, pady=10, sticky='nsew')
        self.scrollbar_chatgpt.grid(row=3, column=3, sticky='ns', pady=10)

        # Permite que los widgets se ajusten al cambiar el tamaño de la ventana
        self.windows.rowconfigure(3, weight=1)

    def find_in_browser(self):
        message = self.entry_message.get()
        self.text_result.insert(tk.END, message)
        self.text_result.insert(tk.END, f" --Recopilando información de la URL {message}")
        self.page_content = self.app_controller.find_in_browser(message)
        self.create_chatgpt_interface()

    def send_chatgpt_question(self):
        question = self.entry_chatgpt_question.get()
        result = self.app_controller.send_chatgpt_question(question, self.page_content)
        self.text_chatgpt_result.insert(tk.END, result)
        self.show_execution_prompt("OK")

    def show_execution_prompt(self, script_description):
        prompt_window = tk.Toplevel(self.windows)
        prompt_window.title("Ejecutar script")

        description_label = tk.Label(prompt_window, text="Ejecutar script", wraplength=300)
        description_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        yes_button = tk.Button(prompt_window, text="Sí", command=self.execute_script)
        yes_button.grid(row=1, column=0, padx=10, pady=10)

        no_button = tk.Button(prompt_window, text="No", command=prompt_window.destroy)
        no_button.grid(row=1, column=1, padx=10, pady=10)


    def execute_script(self):
        os.system("python responseGPT.py")
