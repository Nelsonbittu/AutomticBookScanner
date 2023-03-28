import os
from PIL import Image
import PyPDF2

# Set directory path to the processed images
directory = './processed_images/'

# Get list of image filenames in directory
image_files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

# Sort image filenames in ascending order
image_files.sort()

# Create PDF file
pdf_file = PyPDF2.PdfFileWriter()

# Loop through image files and add each to PDF file
for image_file in image_files:
    # Open image and convert to PDF page
    image = Image.open(directory + image_file)
    pdf_page = PyPDF2.pdf.PageObject.createFromImage(image)
    
    # Add PDF page to PDF file
    pdf_file.addPage(pdf_page)
    
# Save PDF file
with open('combined.pdf', 'wb') as f:
    pdf_file.write(f)
