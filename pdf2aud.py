import pyttsx3
import PyPDF4
import os

f = open('book.pdf','rb')
p_read = PyPDF4.PdfFileReader(f)
pages = p_read.numPages

play = pyttsx3.init()
print('Audio Boook running...')

for i in range(0,#last_page_number):
    page = p_read.getPage(i)
    data = page.extractText()
    play.say(data)
    play.runAndWait()
