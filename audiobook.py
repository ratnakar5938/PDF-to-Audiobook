import pyttsx3
import PyPDF2
from tkinter.filedialog import *

file_path = askopenfilename()
pdf_reader = PyPDF2.PdfFileReader(file_path)
pages = pdf_reader.numPages

for num in range(0, pages):
    page = pdf_reader.getPage(num)
    text = page.extractText()
    player = pyttsx3.init()
    player.say(text)
    player.runAndWait()