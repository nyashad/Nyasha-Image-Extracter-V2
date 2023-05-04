#Import required dependencies
import fitz
import os
from PIL import Image

#Define path to PDF file
file_path = 'sample.pdf'

#Open PDF file
pdf_file = fitz.open(file_path)

#Calculate number of pages in PDF file
page_nums = len(pdf_file)

#Create empty list to store images information
images_list = []

#Extract all images information from each page
for page_num in range(page_nums):
    page_content = pdf_file[page_num]
    images_list.extend(page_content.get_images())

print(images_list)
