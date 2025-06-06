# Bender - Asistente de Extracción y Resumen Automatizado de Contenido Web

**Nombre del proyecto:** Bender (en homenaje al robot de Futurama)  
**Lenguaje base:** Python  
**Interfaz gráfica:** Tkinter  
**Propósito:** Automatizar el scraping y consulta contextual a ChatGPT de contenido técnico web

---

## Descripción General

**Bender** es una herramienta desarrollada con Python que permite al usuario interactuar con una interfaz gráfica minimalista (basada en `Tkinter`) para automatizar la lectura, análisis y consulta de contenido web. Su objetivo principal es facilitar la comprensión de documentación técnica o tutoriales, como aquellos que explican el consumo de APIs, permitiendo un acceso rápido a resúmenes inteligentes mediante el modelo ChatGPT.

---

## ¿Cómo funciona?

El flujo del programa es el siguiente:

1. **Interfaz de entrada de URL:**  
   El usuario introduce una URL en un campo de texto. Generalmente, se trata de una página con un tutorial técnico, documentación, o artículo explicativo.

2. **Scraping del contenido:**  
   Bender realiza automáticamente el scraping del contenido textual de la página web proporcionada, extrayendo la información principal y eliminando elementos irrelevantes (menús, banners, scripts, etc.).

3. **Formateo del prompt:**  
   El contenido extraído se organiza y formatea para ser enviado como *prompt* al modelo de lenguaje de OpenAI (ChatGPT). El formato puede incluir encabezados, código fuente, descripciones y preguntas implícitas.

4. **Consulta a la API de ChatGPT:**  
   Se realiza una petición HTTP a la API de OpenAI, enviando el contenido formateado como prompt y esperando una respuesta generada automáticamente por el modelo.

5. **Presentación del resultado:**  
   La respuesta recibida de ChatGPT se presenta en la parte inferior de la interfaz gráfica, permitiendo al usuario leer de forma directa el resumen, explicación o respuesta generada.

---

## Objetivo del Proyecto

Automatizar el proceso de comprensión de contenido técnico web mediante:

- Extracción rápida y precisa del contenido de una URL
- Generación de un prompt útil a partir del contenido extraído
- Consulta inteligente a un modelo LLM de OpenAI
- Presentación de la respuesta en tiempo real

---

## Tecnologías Utilizadas

- **Python 3.x**
- **Tkinter** – Para la interfaz gráfica
- **Requests / urllib / BeautifulSoup** – Para el scraping del contenido web
- **OpenAI API** – Para el envío del prompt y recepción de respuestas desde ChatGPT

---

## Casos de uso comunes

- Obtener una explicación rápida de un tutorial de consumo de API REST
- Comprender código fuente incluido en artículos técnicos
- Resumir documentación extensa o técnica sin leerla manualmente
- Generar respuestas o aclaraciones a partir de la lectura automatizada de contenido

---

## Estado del proyecto

**En desarrollo activo** – funcionalidades base completas.  
Se planea implementar en versiones futuras:

- Mejor manejo de páginas con JavaScript dinámico
- Selección de secciones específicas del contenido a analizar
- Configuración avanzada del prompt enviado a la API

---

## Licencia

Este proyecto está bajo licencia privada del autor.  
Para uso interno, educativo o colaboraciones, contactar al desarrollador.
