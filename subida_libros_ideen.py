from spire.pdf import *
from spire.pdf.common import *

# Create a PdfDocument object
doc = PdfDocument()

# Load a PDF file
doc.LoadFromFile("./Actualizaciones en endocrinologia glandulas suprerrenales.pdf")

# Get the document information
information = doc.DocumentInformation

# Read built-in properties
print("Author: " + information.Author)
print("Title: " + information.Title)
print("Subject: " + information.Subject)
print("Keywords: " + information.Keywords)
print("Producer: " + information.Producer)

# Close document
doc.Close()